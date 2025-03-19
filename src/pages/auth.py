from src.pages.account import AccountPage
from src.pages.base import BasePage
from src.pages.elements import WebElement


class AuthPage(BasePage):
    cookies_path = r'C:\Users\ASUS\PycharmProjects\Rostelecom-Graduation-project\my_cookies.txt' # my_cookies.txt file path
    _path_url = "/auth"

    def __init__(self, driver):
        super().__init__(driver, self._path_url)
        self._driver = driver
        self.url = self.BASE_URL + self._path_url

        # initialize elements
        self.title = WebElement(self._driver, id="card-title")

        self.tab_phone = WebElement(self._driver, id="t-btn-tab-phone")
        self.tab_mail = WebElement(self._driver, id="t-btn-tab-mail")
        self.tab_login = WebElement(self._driver, id="t-btn-tab-login")
        self.tab_account_number = WebElement(self._driver, id="t-btn-tab-ls")

        self.username = WebElement(self._driver, id="username")
        self.username_placholder = WebElement(self._driver, xpath='//div[@class="rt-input rt-input--rounded rt-input--orange"]/span')

        self.password = WebElement(self._driver, id="password")
        self.eye = WebElement(self._driver, xpath='//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div[2]')

        self.checkbox = WebElement(self._driver, class_name="rt-checkbox__shape rt-checkbox__shape--rounded rt-checkbox__shape--orange")
        self.remember_me_checkbox = WebElement(self._driver, class_name="rt-checkbox")
        self.remember_me_checkbox_checked = WebElement(self._driver, class_name="rt-checkbox rt-checkbox--checked")

        self.login_button = WebElement(self._driver, id="kc-login")

        self.user_agreement_link = WebElement(self._driver, link_text="пользовательского соглашения")

        self.register_link = WebElement(self._driver, id="kc-register")

        self.help_link = WebElement(self._driver, link_text="Помощь")
        self.help_header = WebElement(self._driver, class_name="faq-modal__title")


        self.error_message = WebElement(self._driver, id="form-error-message")

        self.error_empty_email = WebElement(self._driver, id="username-meta")


    def login(self, email, password, tab='mail'):
        self.wait_page_loaded()
        match tab:
            case 'mail':
                self.tab_mail.click()
            case 'login':
                self.tab_login.click()
            case 'phone':
                self.tab_phone.click()
            case 'account number':
                self.tab_account_number.click
        self.username.send_keys(email)
        self.password.send_keys(password)
        self.login_button.click()
        self.wait_page_loaded()
        return AccountPage(self._driver)

    def login_test(self, email, password, tab='mail'):
        self.wait_page_loaded()
        match tab:
            case 'mail':
                self.tab_mail.click()
            case 'login':
                self.tab_login.click()
            case 'phone':
                self.tab_phone.click()
            case 'account number':
                self.tab_account_number.click
        self.tab_mail.click()
        self.username.send_keys(email)
        self.password.send_keys(password)
        self.login_button.click()
        self.wait_page_loaded()




