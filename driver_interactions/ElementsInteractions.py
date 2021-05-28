from traceback import print_stack

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

import utilities.Logger as Log

class ElementsInteractions:

    log = Log.func_logger()

    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_type):
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + locator_type + " entered is not found")
        return False

    def launch_web_page(self, url):
        try:
            self.driver.get(url)
            self.log.info("Web page launched with URL : " + url)
        except Exception:
            self.log.info("Web page not launched with URL : " + url)

    def verify_page(self, page_name):
        assert page_name != self.driver.title, self.take_screenshot(self.driver.title)

    def explicit_wait(self, locator_value, locator_type, time):
        try:
            locator_by_type = self.locator(locator_type)
            WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located((locator_by_type, locator_value)))
            self.log.info("Element found with locator " + locator_value + " using locatorType " + locator_by_type)
        except Exception:
            self.log.error(
                "Element not found with locator " + locator_value + " using locatorType " + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False


    def get_element(self, locator_value, locator_type):
        element = None
        try:
            locator_by_type = self.locator(locator_type)
            element = self.driver.find_element(locator_by_type, locator_value)
            self.log.info("Element found with locator " + locator_value + " using locatorType " + locator_by_type)
        except Exception:
            self.log.error(
                "Element not found with locator " + locator_value + " using locatorType " + locator_type)
            print_stack()
        return element

    def get_all_elements(self, locator_value, locator_type):
        elements = None
        try:
            locator_by_type = self.locator(locator_type)
            elements = self.driver.find_elements(locator_by_type, locator_value)
            self.log.info("Elements found with locator " + locator_value + " using locatorType " + locator_by_type)
        except Exception:
            self.log.error(
                "Elements not found with locator " + locator_value + " using locatorType " + locator_type)
            print_stack()
        return elements

    def wait_element(self, locator_value, locator_type):
        try:
            locator_by_type = self.locator(locator_type)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            element = wait.until(ec.presence_of_element_located((locator_by_type, locator_value)))
            self.log.info("Element found with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Element not found with locator value " + locator_value + " using locatorType " + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False
        return element

    def click_element(self, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.click()
            self.log.info(
                "Clicked on element with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to click on element with locator value " + locator_value + " using locatorType " + locator_type)
            print_stack()
            assert False

    def send_text(self, text, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.send_keys(text)
            self.log.info(
                "Sent the text " + text + " in element with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to sent the text " + text + " in element with locator value " + locator_value + "using locatorType " + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False

    def get_text(self, locator_value, locator_type):
        element_text = None
        try:
            element = self.wait_element(locator_value, locator_type)
            element_text = element.text
            self.log.info(
                "Got the text " + element_text + " from element with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to get the text " + element_text + " from element with locator value " + locator_value + "using locatorType " + locator_type)
            print_stack()

        return element_text

    def select_by_value(self, locator_value, locator_type, value):
        try:
            element = self.wait_element(locator_value, locator_type)
            Select(element).select_by_value(value)
            self.log.info(
                "Selected element with locator value " + locator_value + " using locatorType " + locator_type)
        except Exception:
            self.log.error(
                "Unable to selected element with locator value " + locator_value + " using locatorType " + locator_type)
            print_stack()
            assert False

    def take_screenshot(self, text):
        self.driver.get_screenshot_as_png(text)
