import unittest
from selenium import webdriver

from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout import Page_Checkout
from pages.page_checkout_II import Page_Checkout_II
from pages.page_checkout_complete import Page_Checkout_Complete
class Compras(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5) 
        self.driver.get('https://www.saucedemo.com')
        page_login = Page_Login(self.driver)
        page_login.login('standard_user','secret_sauce')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
    
    def testCurso(self):
        page_inventory = Page_Inventory(self.driver)
        page_inventory.select_element('onesie')
        page_inventory.select_element('fleece')
        page_inventory.go_to_cart()

        page_cart = Page_Cart(self.driver)
        page_cart.go_to_checkout()

        page_checkout = Page_Checkout(self.driver)
        page_checkout.checkout('Fer','Mosqueira','1107')

        page_checkout_II = Page_Checkout_II(self.driver)
        article = page_checkout_II.verify_element(0)
        self.assertEqual('Sauce Labs Onesie', article)
        article = page_checkout_II.verify_element(1)
        self.assertEqual('Sauce Labs Fleece Jacket', article)
        page_checkout_II.finish()
        
        page_checkout_complete = Page_Checkout_Complete(self.driver)
        message = page_checkout_complete.get_final_message()

        self.assertEqual('Thank you for your order!', message)

    def test_order_name_desc(self):
        page_inventory = Page_Inventory(self.driver)
        page_inventory.select_order_by_value('lohi')

if __name__ == '__main__':
    unittest.main()
    