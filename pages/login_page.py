from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_FIELD = (By.CLASS_NAME, "oxd-input")
    PASSWORD_FIELD = (By.CLASS_NAME, "oxd-input")
    LOGIN_BUTTON = (By.CLASS_NAME, "oxd-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "oxd-alert-content")  
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header")
    RESET_PASSWORD_USERNAME_FIELD = (By.CLASS_NAME, "oxd-input")
    RESET_PASSWORD_BUTTON = (By.CLASS_NAME, "oxd-button")
    CANCEL_BUTTON = (By.CLASS_NAME, "oxd-button")
    LOGIN_BANNER = (By.CLASS_NAME, "orangehrm-login-branding")
    USER_DROP_DOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT = (By.CLASS_NAME, "oxd-userdropdown-link")
    RESET_SUCCESS_MESSAGE = (By.CLASS_NAME, "orangehrm-forgot-password-title")


    def enter_username(self, username):
        username_input = self.driver.find_elements(*self.USERNAME_FIELD)[0]
        time.sleep(1)
        username_input.send_keys(username)
        time.sleep(1)

    def enter_password(self, password):
        password_input = self.driver.find_elements(*self.PASSWORD_FIELD)[1]
        time.sleep(1)
        password_input.send_keys(password)
        time.sleep(1)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(1)

    def is_error_message_displayed(self):
        try:
            time.sleep(1)
            error_message = self.driver.find_element(*self.ERROR_MESSAGE)
            return error_message.is_displayed()
        except NoSuchElementException:
            return False

    def is_banner_visible(self):
        try:
            time.sleep(1)
            return self.driver.find_element(*self.LOGIN_BANNER).is_displayed()
            
        except NoSuchElementException:
            return False

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
        time.sleep(1)

    def is_reset_password_page_loaded(self):
        try:
            return self.driver.find_element(*self.RESET_PASSWORD_USERNAME_FIELD).is_displayed()
        except NoSuchElementException:
            return False

    def reset_password(self, username):
        username_input = self.driver.find_element(*self.RESET_PASSWORD_USERNAME_FIELD)
        time.sleep(1)
        username_input.send_keys(username)
        time.sleep(1)
        self.driver.find_elements(*self.RESET_PASSWORD_BUTTON)[1].click()
        time.sleep(1)
        
    def is_reset_success_message_displayed(self):
        try:
            success_message = self.driver.find_element(*self.RESET_SUCCESS_MESSAGE)
            time.sleep(1)
            return success_message.is_displayed()
        except NoSuchElementException:
            return False
    def cancel_reset(self):
        self.driver.find_elements(*self.CANCEL_BUTTON)[0].click()
        time.sleep(1)
    def logout(self):
        self.driver.find_element(*self.USER_DROP_DOWN).click()
        time.sleep(1)
        self.driver.find_elements(*self.LOGOUT)[3].click()
        time.sleep(1)
