import os
import pickle

from base import BasePage
from src.pages.elements import WebElement


class AuthPage(BasePage):


    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends1.herokuapp.com/'
        super().__init__(driver, url)
        with open('my_cookies.txt', 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)
         driver.refresh()

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








