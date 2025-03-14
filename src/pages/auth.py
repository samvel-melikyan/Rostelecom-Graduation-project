import os
import pickle

from settings import *
from src.pages.account import AccountPage
from src.pages.base import BasePage
from src.pages.elements import WebElement
from tests.conftest import web_browser


class AuthPage(BasePage):
    cookies_path = r'C:\Users\User\PycharmProjects\Rostelecom-AutoTests\ my_cookies.txt'

    path_url = "/auth"

    def __init__(self, driver):
        super().__init__(driver, self.path_url)
        self._driver = driver
        self.current_url = self.BASE_URL + self.path_url
        # with open(self.cookies_path, 'rb') as cookiesfile:
        #  cookies = pickle.load(cookiesfile)
        #
        # for cookie in cookies:
        #      driver.add_cookie(cookie)
        #      driver.refresh()

        # initialize elements
        self.title = WebElement(self._driver, id="card-title")

        self.tab_phone = WebElement(self._driver, id="t-btn-tab-phone")
        self.tab_mail = WebElement(self._driver, id="t-btn-tab-mail")
        self.tab_login = WebElement(self._driver, id="t-btn-tab-login")
        self.tab_account_number = WebElement(self._driver, id="t-btn-tab-ls")

        self.username = WebElement(self._driver, id="username")
        self.username_placholder = WebElement(self._driver, xpath='//div[@class="rt-input rt-input--rounded rt-input--orange"]/span')

        self.password = WebElement(self._driver, id="password")

        self.eye = WebElement(self._driver, CLASS="rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye")

        self.remember_me_checkbox = WebElement(self._driver, id="kc-login")

        self.login_button = WebElement(self._driver, id="kc-login")

        self.user_agreement_link = WebElement(self._driver, link_text="пользовательского соглашения")

        self.register_link = WebElement(self._driver, id="kc-register")

        self.help_link = WebElement(self._driver, link_text="Помощь")


    def login(self, email, password):
        self.get_url()
        self.tab_mail.click()
        self.username.send_keys(email)
        self.password.send_keys(password)
        self.login_button.click()
        self.wait_page_loaded()
        return AccountPage(self._driver)





