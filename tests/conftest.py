import uuid

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def driver():
    """Setup WebDriver for Firefox"""
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=DEBUG")

    # service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def firefox_options():
    """Setup Firefox options"""
    options = Options()
    options.binary = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    # options.add_argument("-headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=DEBUG")
    return options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Detect test failures and pass info to teardown"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def web_browser(request, driver):
    """Setup web browser instance"""
    browser = driver
    browser.set_window_size(1400, 1000)
    yield browser
    if request.node.rep_call.failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")
            screenshot_path = f'screenshots/{uuid.uuid4()}.png'
            browser.save_screenshot(screenshot_path)
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
            print(f'URL: {browser.current_url}')
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except Exception as e:
            print(f"Error capturing screenshot: {e}")


def get_test_case_docstring(item):
    """Format docstring for human-readable test case names"""
    full_name = ''
    if item._obj.__doc__:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        if hasattr(item, 'callspec'):
            params = item.callspec.params
            res_keys = sorted([k for k in params])
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """Modify test case names during execution"""
    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """Modify test case names when using --collect-only"""
    if session.config.option.collectonly:
        for item in session.items:
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)
        pytest.exit('Done!')
