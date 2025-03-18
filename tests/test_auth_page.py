from operator import indexOf

import pytest

from settings import *
from src.pages.account import AccountPage
from src.pages.auth import AuthPage
from tests.conftest import web_browser


class TestAuthPage:

    def test_auth_page_is_available(self, web_browser):
        auth_page = AuthPage(web_browser)
        text = auth_page.title.get_text()
        assert text == "Авторизация", "Wrong page title"

    def test_choose_phone_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.tab_phone.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Мобильный телефон', "Username field is not presented"

    def test_choose_mail_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.tab_mail.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Электронная почта', "Username field is not presented"

    def test_choose_login_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.tab_login.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Логин', "Username field is not presented"

    def test_choose_account_number_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.tab_account_number.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Лицевой счёт', "Username field is not presented"

    def test_login_with_valid_email_credentials(self, web_browser):
        auth_page = AuthPage(web_browser)
        account_page = auth_page.login(valid_email, valid_password)
        name = account_page.user_name.get_text()
        assert name == user_name, "Login failed"

    @pytest.mark.negative
    @pytest.mark.parametrize("email, password", [
        (valid_email, valid_password[:8]),
        (unregisered_email, valid_password),
        # ('', ''),
        # ('', valid_password),
        # (valid_email, ''),
        (valid_email.replace('@', ''), valid_password),
        (valid_email[-4], valid_password),
        (valid_email[:valid_email.index('@')], valid_password),
        (valid_email, valid_password[:5])], ids=[
        'incorrect_password', 'unregistered_email', 'email without @ symbol',
        'email without TLD', 'email without domain name and TLD', 'short_password'])
    def test_login_with_invalid_email_credentials(self, web_browser, email, password):
        auth_page = AuthPage(web_browser)
        auth_page.login_test(email, password)
        current_url = web_browser.current_url[:len(auth_page.url)]
        assert current_url == auth_page.url, "Login with empty or invalid credentials passed"
        assert auth_page.error_message.is_presented(), "login with invalid credentials passed"


    @pytest.mark.negative
    @pytest.mark.parametrize("email, password", [
        ('', valid_password),
        (valid_email, ''),
        ('', '')], ids=[
        'without email', 'without password', 'empty email and password'])
    def test_login_with_empty_email_credentials(self, web_browser, email, password):
        auth_page = AuthPage(web_browser)
        auth_page.login_test(email, password)
        current_url = web_browser.current_url[:len(auth_page.url)]
        assert current_url == auth_page.url, "Login with empty or invalid credentials passed"
        assert (auth_page.error_empty_email.is_presented()
                or auth_page.error_empty_email.is_presented()), "login with "

    def test_functionality_of_remember_me_checkbox(self, web_browser):
        auth_page = AuthPage(web_browser)
        try:
            auth_page.remember_me_checkbox.is_presented()
            auth_page.checkbox.click()
        except AttributeError:
            auth_page.remember_me_checkbox_checked.is_presented()
        web_browser.execute_script("window.open('');")
        web_browser.switch_to.window(web_browser.window_handles[1])
        account_page = AccountPage(web_browser)
        name = account_page.user_name.get_text()
        assert name == user_name, "Login failed"




