# Import useful items from various Libraries
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import re

# Create a function
def instahyre_scrape(url, num):
    # Create empty lists of Columns required in the dataframe
    data = {
        'Name': [],
        'Location': [],
        'Founded': [],
        'Employees': [],
        'About': [],
        'Skills': [],
        'Link': []
    }

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    # Loop through pages until the desired number of Job Listings is reached
    while len(data['Name']) < num:
        # Extracting Job Listings
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_listings = soup.find_all('div', class_='employer-row')

        for i, job in enumerate(job_listings):

            # Extracting Job Title
            name = job.find('div', class_='employer-job-name').text.strip()

            # Extracting Job Location
            location = job.find('div', class_='employer-locations').text.strip()

            # Extracting Foundation Year and Number of Employees
            employer_info_div = job.find('div', class_='employer-info')

            # Find all spans within the employer_info_div
            spans = employer_info_div.find_all('span', class_='ng-scope')

            # Initialize variables for Founded and Employees
            founded = ''
            employees = ''

            # Loop through the spans and extract information
            for span in spans:
                if 'Founded' in span.text:
                    # Extract Founded year and filter out non-numeric characters
                    founded_span = span.find_next('span', class_='ng-binding')
                    founded = ''.join(filter(str.isdigit, founded_span.text.strip())) if founded_span else ''
                elif 'employees' in span.text:
                    # Extract Employees count and handle ranges or descriptions
                    employees_span = span.find_next('span', class_='ng-binding')
                    employees_text = employees_span.text.strip() if employees_span else ''

                    # Use regular expressions to extract numeric information
                    range_match = re.search(r'(\d+)\s*-\s*(\d+)|More than (\d+)', employees_text)

                    if range_match:
                        if range_match.group(1) and range_match.group(2):
                            # Use the average of the range
                            employees = (int(range_match.group(1)) + int(range_match.group(2))) // 2
                        elif range_match.group(3):
                            # Use the specified number for "More than"
                            employees = int(range_match.group(3))
                    else:
                        # If no match, try extracting any numeric value
                        employees = ''.join(filter(str.isdigit, employees_text))

                        # Convert employees to integer if it contains numeric values
                        employees = int(employees) if employees.isdigit() else None

            # Convert founded and employees to integers if they contain numeric values
            founded = int(founded) if founded.isdigit() else None
            # employees = int(employees) if isinstance(employees, str) and employees.isdigit() else employees

            # Extract About the job role
            about_div = job.find('div', class_='employer-notes ng-binding ng-scope')

            # Check if the about_div element was found
            about = about_div.text.strip() if about_div else ''

            # Extracting skills information
            skills_div = job.find('div', class_='job-skills ng-scope')
            skills_ul = skills_div.find('ul', class_='tags candidate-opp-keywords')

            skills_list = []

            # Extract all skills from the li elements within the ul
            if skills_ul:
                for li in skills_ul.find_all('li', class_='ng-binding ng-scope'):
                    # Append all skills to the existing skills list
                    skill_text = li.text.strip()
                    skills_list.append(skill_text)

            # Extract link information
            link_div = driver.find_elements(By.CSS_SELECTOR, 'div.opportunity-action-links a')
            link = link_div[i].get_attribute('href') if link_div else ''

            # Appending the data in the respective lists

            data['Name'].append(name)
            data['Location'].append(location)
            data['Founded'].append(founded)
            data['Employees'].append(employees)
            data['About'].append(about)
            data['Skills'].append(skills_list)
            data['Link'].append(link)

            # Check if we have enough listings
            if len(data['Name']) >= num:
                break

        # If there are more listings, find and click the next page button
        if len(data['Name']) < num:
            try:
                next_page_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[21]/li[12]")
                next_page_button.click()
                time.sleep(5)
            except Exception as e:
                print(f"Error while clicking next page button: {e}")
                break

    # Close the Web Driver
    driver.quit()

    return data

# URL of website from where data is to be extracted
url = "https://www.instahyre.com/python-jobs"

# Number of Data to be Extracted
num_to_scrape = 300

# Passing the values to function
dataset = instahyre_scrape(url, num_to_scrape)

# Converting the extracted dat into DataFrame using Pandas
df = pd.DataFrame(dataset)

# Converting the DataFrame to CSV File
df.to_csv('instahyre_data.csv', index=False)

current_directory = os.getcwd()
print(current_directory)
