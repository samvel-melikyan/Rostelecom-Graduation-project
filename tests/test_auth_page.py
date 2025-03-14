from settings import *
from src.pages.account import AccountPage
from src.pages.auth import AuthPage
from tests.conftest import web_browser


class TestAuthPage:

    def test_auth_page_is_available(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.get_url(auth_page.path_url)
        text = auth_page.title.get_text()
        assert text == "Авторизация", "Wrong page title"

    def test_choose_phone_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.get_url(auth_page.path_url)
        auth_page.tab_phone.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Мобильный телефон', "Username field is not presented"

    def test_choose_mail_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.get_url(auth_page.path_url)
        auth_page.tab_mail.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Электронная почта', "Username field is not presented"

    def test_choose_login_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.get_url(auth_page.path_url)
        auth_page.tab_login.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Логин', "Username field is not presented"

    def test_choose_account_number_tab(self, web_browser):
        auth_page = AuthPage(web_browser)
        auth_page.get_url(auth_page.path_url)
        auth_page.tab_account_number.click()
        placeholder = auth_page.username_placholder.get_text()
        assert placeholder == 'Лицевой счёт', "Username field is not presented"

    def test_login_with_valid_email_credentials(self, web_browser):
        auth_page = AuthPage(web_browser)
        account_page = auth_page.login(valid_email, valid_password)
        account_page.get_url()
        name = account_page.user_name.get_text()
        assert name == 'Ресалтваниюсн Саливан', "Login failed"
