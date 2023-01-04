from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.elements import Elements
from resources.constants import *
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.elements = Elements()

    def wait_and_get_element(self, element_locator, by=By.CSS_SELECTOR, time_out=5):
        """
        wait and get element from the screen, block until given time out
        :param element_locator: (str) element locator
        :param by: Element Selector types
        :param time_out: (int) defaults to 5 sec

        :return: (WebElement) target_element
        """

        element = WebDriverWait(self.driver, time_out).until(
            expected_conditions.presence_of_element_located((by, element_locator)))

        if not element:
            raise Exception(ELEMENT_NOT_FOUND.format(element_locator, None))
        return element

    def click_and_select_dropdown(self, value):
        self.value = value
        dd = Select(self)
        dd.select_by_visible_text(self.value)
