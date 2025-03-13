from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from tests.conftest import web_browser
from src.pages.auth import AuthPage
BASE_URL = "https://b2c.passport.rt.ru"



class TestAuthPage:

    def test_auth_page_is_available(self, web_browser):
        page = AuthPage(web_browser)
        element = WebDriverWait(web_browser, 10).until(
            EC.presence_of_element_located((By.ID, 'card-title')))
        print(element.text)
        # print(type(page.title.get_text()))
        # assert page.title is not None

        # text = page.title.get_text()
        # assert text == "Авторизация"

# ToDo need to fully rewrite elements
