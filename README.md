# OrangeHRM Login Automation with Selenium

## Overview
This project automates the login process and tests several login scenarios for the OrangeHRM platform using Selenium WebDriver in Python. It includes test cases for:

- Logging in with valid credentials
- Handling invalid credentials
- Using the "Forgot Password" functionality
- Redirecting to the login page after cancelling password reset
- Verifying login page banner visibility

## Project Structure
- `data/TestData.py`: Contains test data, including the URL, valid and invalid credentials, and driver path.
- `pages/login_page.py`: Defines the page object model for the login page, including all related actions (login, logout, reset password).
- `tests`: Main folder where test cases are executed.

## Prerequisites
- Python 3.x
- Selenium package (`pip install selenium`)
- Google Chrome browser
- ChromeDriver (Ensure the version matches your Chrome version; update `DRIVER_PATH` in `TestData.py`)

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/r0bxz/OrangeHRM-Login-Automation-with-Selenium.git
    cd OrangeHRM-Login-Automation-with-Selenium
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Update the `TestData.py` file with:
   - The path to your `chromedriver.exe`
   - The URL for OrangeHRM
   - Valid and invalid login credentials

## Running the Tests
Run the main test script:
```bash
python tests.main
