from src.pages.base import BasePage
from src.pages.elements import WebElement


class AccountPage(BasePage):
    path_url = "/account_b2c/page"
    def __init__(self, driver):
        super().__init__(driver, self.path_url)
        self._driver = driver
        self.url = self.BASE_URL + self.path_url


        # initialize elements
        self.user_name = WebElement(self._driver, tag_name="h2")

    def get_page(self):
        self._driver.get(self.url)
        self.wait_page_loaded()