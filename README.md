# Job Analytics

URL =  https://www.instahyre.com/python-jobs

**Objective**: In this project, I will utilize Python web scraping to extract **more than** **300 job listings** related to Python roles from the Instahyre website. Their task is to create a dataset comprising specific details for each job listing.

Table 1 : `jobs`

**Data Description**:

1. **Name**:
    - *Data Type*: String
    - *Description*: Title or name of the job position.
2. **Location**:
    - *Data Type*: String
    - *Description*: Location or city associated with the job posting.
3. **Founded**:
    - *Data Type*: Integer or String
    - *Description*: Year of establishment of the company offering the job
4. **Employees**:
    - *Data Type*: Integer or String
    - *Description*: Number of employees in the company.
5. **About**:
    - *Data Type*: String
    - *Description*: Brief information or description about the company.
6. **Skills**:
    - *Data Type*: List of Strings
    - *Description*: Skills or requirements for the job position.
7. **Link**:
    - *Data Type*: String (URL)
    - *Description*: Link to the job listing for additional details or application.

All the details can be found on the link -https://www.instahyre.com/python-jobs

**General Instructions for Python Web Scraping Assignment - Job Analytics** 

**Ethical Scraping Practices**:

- Always adhere to ethical scraping practices and respect the terms of service of the website.
- Avoid making too many requests in a short period to prevent overloading the website's servers.
- Be mindful of web scraping etiquette to avoid putting unnecessary load on the website's servers.

**Code Documentation**:

- Include comments in your Python script to explain each step of the web scraping process.
- Clearly mention the purpose of each function or block of code.

**Readability and Style**:

- Write clean and readable code
- Use meaningful variable and function names to enhance code clarity.

**Respectful Scraping**:

- Use a reasonable delay between requests to avoid putting unnecessary load on the IMDb servers.
- Be considerate of the website's resources and do not engage in aggressive scraping practices

**Dataset Creation**:

- Create a dataset using the **`pandas`** library or `file handling` method to organize the scraped data.
- Include columns for 'name', 'location', 'founded', 'employees', 'about', 'skills', 'link’

### Data Cleaning

After successfully scraping the data, a critical step was performed to enhance the quality and reliability of the dataset. This involved a thorough examination and cleaning process to address potential issues that could impact the accuracy of our analyses and insights.

**Key Data Cleaning Steps:**

1. **Handling Null Values:**
    - Identified and addressed missing values within the dataset, employing appropriate techniques for imputation based on statistical measures.
2. **Duplicate Values Removal:**
    - Detected and eliminated duplicate records to ensure the dataset is free from redundant information, preventing skewed analyses.

 3.   **Data Type Standardization:**

- Ensured appropriate data types for variables, such as converting numerical variables to the correct numeric data types and standardizing date formats.

### Data Visualization

Following the data cleaning phase, a comprehensive data visualization process was undertaken to transform raw data into meaningful insights that are easily interpretable and actionable. Visualization is a powerful tool for conveying complex information in a clear and visually engaging manner.

**Key Data Visualization Steps:**

1. **Exploratory Data Analysis (EDA):**
    - Conducted exploratory data analysis to uncover key statistics, trends, and patterns within the dataset, providing an initial understanding of the data's characteristics.
2. **Correlation Analysis:**
    - Explored relationships and correlations between different variables, revealing patterns that contribute to a deeper understanding of the data.
3. **Pattern Recognition:**
    - Identified recurring patterns and themes within the dataset, enabling the extraction of meaningful insights and trends.  
4. **Skill and Technology Trends Visualization:**
    - Created visual representations to highlight the demand for various skills and technologies across job listings, facilitating a clear understanding of market trends.
5. **Geographical Analysis Representation:**
    - Utilized visualizations, such as bar charts or maps, to display the distribution of job opportunities across different locations, aiding in the identification of regional trends.

 6.  ************Bonus:************

- In addition to the fundamental data cleaning and visualization steps, a further exploration of the dataset yielded valuable supplementary insights. This bonus analysis delves deeper into specific aspects of the data, uncovering additional patterns and trends that contribute to a more comprehensive understanding of the information at hand.

**Helpful Links**

- Basics of HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
- https://pypi.org/project/beautifulsoup4/
- https://beautiful-soup-4.readthedocs.io/en/latest/
- https://www.selenium.dev/selenium/docs/api/py/api.html

![download](https://github.com/aaddii0911/Web-Scrapping/assets/154340466/8e7d0900-3b12-49e4-91c2-7a352b04cd56)
