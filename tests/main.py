from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from data.TestData import TestData
from pages.login_page import LoginPage
import time

def main():
    service = Service(executable_path=TestData.DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(30)
    
    try:
        driver.get(TestData.URL)
        login_page = LoginPage(driver)

        # Test Case 1: Login with valid credentials
        print("Test Case 1: Verify login with valid credentials")
        expected_result = "Dashboard loaded"
        login_page.enter_username(TestData.VALID_USERNAME)
        login_page.enter_password(TestData.VALID_PASSWORD)
        login_page.click_login()
        actual_result = "Dashboard loaded" if "dashboard" in driver.current_url else "Failed to load dashboard"
        print(f"Expected: {expected_result}, Actual: {actual_result}")
        assert "dashboard" in driver.current_url, actual_result
        login_page.logout()  

        # Test Case 2: Login with invalid credentials
        print("\nTest Case 2: Verify login with invalid credentials")
        expected_result = "Error message displayed"
        login_page.enter_username(TestData.INVALID_USERNAME)
        login_page.enter_password(TestData.INVALID_PASSWORD)
        login_page.click_login()
        actual_result = "Error message displayed" if login_page.is_error_message_displayed() else "Error message not displayed"
        print(f"Expected: {expected_result}, Actual: {actual_result}")
        assert login_page.is_error_message_displayed(), actual_result

        # Test Case 3: Click "Forgot Password" link and send reset link
        print("\nTest Case 3: Verify clicking the 'Forgot Password' link")
        expected_result = "A page with 'Reset Password link sent successfully' message should appear"
        login_page.click_forgot_password()
        login_page.reset_password(TestData.VALID_USERNAME)
        # Check for the reset password success message
        actual_result = ("Reset Password link sent successfully" if login_page.is_reset_success_message_displayed() 
            else "Reset Password link message not displayed"
        )
        
        print(f"Expected: {expected_result}, Actual: {actual_result}")
        assert login_page.is_reset_success_message_displayed(), actual_result
        
        # Test Case 4: Press "Cancel" button in reset password page
        print("\nTest Case 4: Verify pressing 'Cancel' button redirects to login page")
        expected_result = "Redirected to login page"
        driver.get(TestData.URL)
        login_page.click_forgot_password()
        login_page.cancel_reset()
        actual_result = "Redirected to login page" if "login" in driver.current_url else "Did not redirect to login page"
        print(f"Expected: {expected_result}, Actual: {actual_result}")
        assert "login" in driver.current_url, actual_result

        # Test Case 5: Check appearance of login page banner
        print("\nTest Case 5: Verify the appearance of login page banner")
        expected_result = "Login banner is visible"
        driver.get(TestData.URL)
        actual_result = "Login banner is visible" if login_page.is_banner_visible() else "Login banner is not visible"
        print(f"Expected: {expected_result}, Actual: {actual_result}")
        assert login_page.is_banner_visible(), actual_result

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
