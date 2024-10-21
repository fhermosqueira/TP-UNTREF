from selenium.webdriver.common.by import By


class Page_Checkout():
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID,'first-name')
        self.last_name = (By.ID,'last-name')
        self.postal_code = (By.ID,'postal-code')
        self.continue_button = (By.ID,'continue')
        self.error_message = (By.CLASS_NAME,'error-message-container')
            
    def full_checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def lastnameerror(self):
        return self.driver.find_element(*self.error_message).text
    
    def postalcodeeerror(self):
        return self.driver.find_element(*self.error_message).text
    
    def checkout_lastname(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.continue_button).click()