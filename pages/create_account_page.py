from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random
import string


button = (By.XPATH, '//*[@class="action submit primary"]')
first_name = (By.ID, 'firstname')
first_name_error = (By.ID, 'firstname-error')
last_name = (By.ID, 'lastname')
last_name_error = (By.ID, 'lastname-error')
email = (By.ID, 'email_address')
email_error = (By.ID, 'email_address-error')
password = (By.ID, 'password')
password_error = (By.ID, 'password-error')
confirm_password = (By.ID, 'password-confirmation')
confirm_password_error = (By.ID, 'password-confirmation-error')
field_error_message = (By.ID, 'password-confirmation-error')


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    def required_fields_error(self, error_message):
        self.driver.maximize_window()
        self.find(button).click()
        first_name_field = self.find(first_name_error)
        last_name_field = self.find(last_name_error)
        email_field = self.find(email_error)
        password_field = self.find(password_error)
        confirm_password_field = self.find(confirm_password_error)
        assert first_name_field.text == error_message
        assert last_name_field.text == error_message
        assert email_field.text == error_message
        assert password_field.text == error_message
        assert confirm_password_field.text == error_message

    def get_random_values(self, length):
        value = ''.join(f'{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_uppercase)}'
                        f'{random.choice(string.digits)}' for i in range(length))
        return value

    def password_confirmation_error(self, error_message):
        value = self.get_random_values(8)
        self.find(first_name).send_keys(value)
        self.find(last_name).send_keys(value)
        self.find(email).send_keys(f'{value}@test.com')
        self.find(password).send_keys(value)
        self.find(confirm_password).send_keys('12345678')
        self.find(button).click()
        message = self.find(field_error_message)
        assert message.text == error_message

    def successful_account_creation(self):
        value = self.get_random_values(8)
        self.find(first_name).send_keys(value)
        self.find(last_name).send_keys(value)
        self.find(email).send_keys(f'{value}@test.com')
        self.find(password).send_keys(value)
        self.find(confirm_password).send_keys(value)
        self.find(button).click()
