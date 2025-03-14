import time
from termcolor import colored

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    _driver = None
    BASE_URL = 'https://b2c.passport.rt.ru'
    def __init__(self, driver, url=''):
        self.current_url = self.BASE_URL + url
        self._driver = driver
        self.get(self.current_url)

    # def __setattr__(self, name, value):
    #     if not name.startswith('_'):
    #         self.__getattribute__(name)._set_value(self._driver, value)
    #     else:
    #         super(BasePage, self).__setattr__(name, value)

    # def __getattribute__(self, item):
    #     attr = object.__getattribute__(self, item)
    #
    #     if not item.startswith('_') and not callable(attr):
    #         attr._driver = self._driver
    #         attr._page = self
    #
    #     return attr

    def get_url(self):
        return self.current_url

    def get(self, url):
        self._driver.get(url)
        self.wait_page_loaded()

    def go_back(self):
        self._driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self._driver.refresh()
        self.wait_page_loaded()

    def screenshot(self, file_name='screenshot.png'):
        self._driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        """ Scroll the page down. """
        if offset:
            self._driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Scroll the page up. """
        if offset:
            self._driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        """ Switch to iframe by it's name. """
        self._driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        """ Cancel iframe focus. """
        self._driver.switch_to.default_content()

    def get_current_url(self):
        """ Returns current browser URL. """
        return self._driver.current_url

    def get_page_source(self):
        """ Returns current page body. """
        source = ''
        try:
            source = self._driver.page_source
        except:
            print(colored('Con not get page source', 'red'))
        return source

    def check_js_errors(self, ignore_list=None):
        """ This function checks JS errors on the page. """

        ignore_list = ignore_list or []

        logs = self._driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:

            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self._driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self._driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self._driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self._driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self._driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self._driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
