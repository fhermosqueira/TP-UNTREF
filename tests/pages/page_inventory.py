from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Page_Inventory():
    def __init__(self, driver):
        self.driver = driver
        self.cart = (By.ID,'shopping_cart_container')
        self.order = (By.CLASS_NAME, 'product_sort_container')
        self.item = (By.CLASS_NAME, 'inventory_item_name')
        self.price = (By.CLASS_NAME, 'inventory_item_price')
        self.cartbutton = (By.CLASS_NAME, 'btn_inventory')
        self.menu = (By.ID, 'react-burger-menu-btn')
        self.logout_button = (By.ID, 'logout_sidebar_link')
          
    def select_element(self, element):
        #pre_element = 'add-to-cart-'+element.replace(' ','-').lower()
        self.driver.find_element(By.ID,'add-to-cart-'+element.replace(' ','-').lower()).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()

    def select_order_by_value(self, value):
        Select(self.driver.find_element(*self.order)).select_by_value(value)
    
    def select_order_by_visible_text(self, text):
        Select(self.driver.find_element(*self.order)).select_by_visible_text(text)

    def select_order_by_index(self,index):
        Select(self.driver.find_element(*self.order)).select_by_index(index)
    
    def get_articles_names(self):
        items = self.driver.find_elements(*self.item)
        texts = []
        for item in items:
            texts.append(item.text)
        return texts
    
    def get_articles_prices(self):
        price_elements = self.driver.find_elements(*self.price)
        prices = []
        for element in price_elements:
            prices.append(element.text)
        return prices
    
    def add_all(self):
        add_to_cart_buttons = self.driver.find_elements(*self.cartbutton)
        for button in add_to_cart_buttons:
            button.click()
        
    def logout(self):
        self.driver.find_element(*self.menu).click()
        self.driver.find_element(*self.logout_button).click()

  




        #1- Ordene de manera descendente
        #2- Devuelvo todos los textos
        #3- Comparo que este todo ordenado