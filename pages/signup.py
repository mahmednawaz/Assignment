import time
from pages.base_page import BasePage
from resources.constants import *


class SignUP(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fname_textbox(self):
        return self.wait_and_get_element(self.elements.fname_css)

    def lname_textbox(self):
        return self.wait_and_get_element(self.elements.lname_css)

    def select_gender(self):
        return self.wait_and_get_element(self.elements.gender_css)

    def select_experience(self):
        return self.wait_and_get_element(self.elements.exp_css)

    def date_textbox(self):
        return self.wait_and_get_element(self.elements.date_css)

    def select_profession(self):
        return self.wait_and_get_element(self.elements.prof_css)

    def select_tool(self):
        return self.wait_and_get_element(self.elements.auto_tool_css)

    def select_continent(self):
        return self.wait_and_get_element(self.elements.continent_css)

    def select_command(self):
        return self.wait_and_get_element(self.elements.selen_comnd_css)

    def click_image_btn(self):
        return self.wait_and_get_element(self.elements.auto_tool_css)

    def click_signup_btn(self):
        return self.wait_and_get_element(self.elements.fname_css)

    def sign_up(self):
        self.fname_textbox().send_keys(fname)
        self.lname_textbox().send_keys(lname)
        self.select_gender().click()
        self.select_experience().click()
        self.date_textbox().send_keys(date)
        self.select_profession().click()
        time.sleep(5)
        self.select_tool().click()
        self.select_continent().click_and_select_dropdown(continent_value)
        self.select_command().click_and_select_dropdown(selem_comnd_value)
        self.select_command()
        self.click_image_btn().send_keys(img_path)
        self.click_signup_btn()
