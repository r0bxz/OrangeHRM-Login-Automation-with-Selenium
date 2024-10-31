Overview
This project automates the login process and tests several login scenarios for the OrangeHRM platform using Selenium WebDriver in Python. It includes test cases for:

Logging in with valid credentials
Handling invalid credentials
Using the "Forgot Password" functionality
Redirecting to the login page after cancelling password reset
Verifying login page banner visibility

Project Structure
data/TestData.py: Contains test data, including the URL, valid and invalid credentials, and driver path.
pages/login_page.py: Defines the page object model for the login page, including all related actions (login, logout, reset password).
tests: Main folder where test cases are executed.

Prerequisites
Python 3.x
Selenium package (pip install selenium)
Google Chrome browser
ChromeDriver (Ensure the version matches your Chrome version; update DRIVER_PATH in TestData.py)

Setup

Clone the repository:

git clone https://github.com/r0bxz/OrangeHRM-Login-Automation-with-Selenium.git
cd OrangeHRM-Login-Automation-with-Selenium
Install the required dependencies:

bash
pip install -r requirements.txt

Update the TestData.py file with:

The path to your chromedriver.exe
The URL for OrangeHRM
Valid and invalid login credentials
Running the Tests
Run the main test script:

bash
python main.py

Test Cases
Login with Valid Credentials: Ensures dashboard access after a successful login.
Login with Invalid Credentials: Verifies error message displays when login fails.
Forgot Password: Tests the functionality to reset password and confirms the success message.
Cancel Reset: Checks if canceling a password reset redirects to the login page.
Banner Visibility: Validates the visibility of the login page banner.
