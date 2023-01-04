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
        fname = self.fname_textbox()
        fname.send_keys(fname)
        lname = self.lname_textbox()
        lname.send_keys(lname)
        gen = self.select_gender()
        gen.click()
        exp = self.select_experience()
        exp.click()
        date = self.date_textbox()
        date.send_keys(date)
        time.sleep(5)
        prof = self.select_profession()
        prof.click()
        time.sleep(5)
        tool = self.select_tool()
        tool.click()
        continent = self.select_continent()
        continent.click_and_select_dropdown(continent_value)
        command=self.select_command()
        command.click_and_select_dropdown(selem_comnd_value)
        self.select_command()
        img = self.click_image_btn()
        img.send_keys(img_path)
        self.click_signup_btn()
