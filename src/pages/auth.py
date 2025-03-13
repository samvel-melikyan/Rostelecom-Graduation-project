import os
import pickle

from src.pages.base import BasePage
from src.pages.elements import WebElement


class AuthPage(BasePage):
    URL = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=382d15e4-a42b-4a53-9f88-1d1cee5552e0"
    cookies_path = r'C:\Users\User\PycharmProjects\Rostelecom-AutoTests\ my_cookies.txt'

    def __init__(self, driver, url=''):
        if url == '':
            self.url = os.getenv("MAIN_URL") or self.URL
        super().__init__(driver, self.url)
        #
        # with open(self.cookies_path, 'rb') as cookiesfile:
        #  cookies = pickle.load(cookiesfile)
        #
        # for cookie in cookies:
        #      driver.add_cookie(cookie)
        #      driver.refresh()

    title = WebElement(id="card-title")

    tab_phone = WebElement(id="t-btn-tab-phone")
    tab_mail = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_account_number = WebElement(id="t-btn-tab-ls")

    username = WebElement(id="username")
    password = WebElement(id="password")

    eye = WebElement(CLASS="rt-base-icon rt-base-icon--fill-path rt-eye-icon rt-input__eye")

    remember_me_checkbox = WebElement(id="kc-login")

    login_button = WebElement(id="kc-login")

    user_agreement_link = WebElement(link_text="пользовательского соглашения")

    register_link = WebElement(id="kc-register")

    help_link = WebElement(link_text="Помощь")








