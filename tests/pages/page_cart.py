from selenium.webdriver.common.by import By

class Page_Cart():
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.ID,'checkout')
        self.item = (By.CLASS_NAME, 'inventory_item_name')
        self.continue_shopbutton = (By.ID, "continue-shopping")
        self.remove_onesiebutton = (By.ID,'remove-sauce-labs-onesie')
               

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_articles_names(self):
        items = self.driver.find_elements(*self.item)
        texts = []
        for item in items:
            texts.append(item.text)
        return texts
    
    def continue_shop(self):
        self.driver.find_element(*self.continue_shopbutton).click()

    def remove_onesie(self):
        self.driver.find_element(*self.remove_onesiebutton).click()
    
  

    