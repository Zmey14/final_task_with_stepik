from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()
        
    # символ *, указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать. 
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present!"