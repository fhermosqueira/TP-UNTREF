import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.firefox.options import Options

from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout import Page_Checkout
from pages.page_checkout_II import Page_Checkout_II
from pages.page_checkout_complete import Page_Checkout_Complete
from selenium.webdriver.common.by import By

class Compras(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('-headless')
        cls.driver = webdriver.Firefox(options = options)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def setUp(self) -> None:
        load_dotenv()
        #base_url = os.getenv('BASE_URL')
        user = os.getenv('USER')
        password = os.getenv('PASS')
        #self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(os.getenv('BASE_URL'))
        page_login = Page_Login(self.driver)
        page_login.login(user,password)
        self.page_inventory = Page_Inventory(self.driver)
        

    #def tearDown(self) -> None:
        #self.driver.close()
        #self.driver.quit()

    def test_case_one(self):
        self.page_inventory.select_order_by_value('lohi')
        prices = self.page_inventory.get_articles_prices()
        prices_float = [float(price.replace('$', '')) for price in prices]
        self.assertEqual(prices_float, sorted(prices_float))
 
    def test_case_two(self):
       self.page_cart = Page_Cart(self.driver)
       self.page_checkout = Page_Checkout(self.driver)
       texts_inv = self.page_inventory.get_articles_names()
       self.page_inventory.add_all()
       self.page_inventory.go_to_cart()
       texts_cart = self.page_cart.get_articles_names()
       self.assertEqual(len(texts_inv),len(texts_cart))
       self.page_cart.go_to_checkout()
       self.page_checkout.full_checkout('Fer','','')    
       message = self.page_checkout.lastnameerror()
       self.assertEqual('Error: Last Name is required',message)
       self.page_checkout.checkout_lastname('Mosqueira')
       message = self.page_checkout.postalcodeeerror()
       self.assertEqual('Error: Postal Code is required',message)

    def test_case_three(self):
        self.page_cart = Page_Cart(self.driver)
        self.page_checkout = Page_Checkout(self.driver)
        self.page_checkout_II = Page_Checkout_II(self.driver)
        self.page_checkout_complete = Page_Checkout_Complete(self.driver)
        self.page_inventory.select_element('sauce labs onesie')
        self.page_inventory.go_to_cart()
        self.page_cart.remove_onesie()
        texts_inv = self.page_inventory.get_articles_names()
        texts_cart = self.page_cart.get_articles_names()
        self.assertEqual(len(texts_inv),len(texts_cart))
        self.page_cart.continue_shop()
        self.page_inventory.select_element('sauce labs onesie')
        self.page_inventory.select_element('sauce labs fleece jacket')
        self.page_inventory.go_to_cart()
        texts_inv = self.page_inventory.get_articles_names()
        texts_cart = self.page_cart.get_articles_names()
        self.assertEqual(len(texts_inv),len(texts_cart))
        self.page_cart.go_to_checkout()
        self.page_checkout.full_checkout('Fer','Mosqueira','1111')   
        self.page_checkout_II.finish()
        message = self.page_checkout_complete.get_final_message()
        self.assertEqual('Thank you for your order!', message)



