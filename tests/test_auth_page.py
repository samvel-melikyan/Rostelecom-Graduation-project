from src.pages.auth import AuthPage
BASE_URL = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=175cc718-90d6-4395-ba45-56c920d6810c&theme=light"
class TestAuthPage:
    def test_auth_page_is_available(self, driver):
        page = AuthPage(driver, BASE_URL)
        assert page.title == "Авторизация"
