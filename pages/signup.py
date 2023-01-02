import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.elements import Elements
from selenium.webdriver.support import expected_conditions as EC


class SignUP:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def fname_textbox(self, fname):
        self.fname = fname
        fname_text_box = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.fname_css)))
        # fname_text_box.click()
        fname_text_box.send_keys(self.fname)

    def lname_textbox(self, lname):
        self.lname = lname
        lname_text_box = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.lname_css)))
        lname_text_box.send_keys(self.lname)

    def select_gender(self):
        select_gen = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.gender_css)))
        select_gen.click()

    def select_experience(self):
        select_exp = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.exp_css)))
        select_exp.click()

    def date_textbox(self, date):
        self.date = date
        date_text_box = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.date_css)))
        date_text_box.send_keys(self.date)

    def select_profession(self):
        time.sleep(5)
        selc_prof = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.prof_css)))
        selc_prof.click()
    def select_tool(self):
        time.sleep(5)
        sel_tol=self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.auto_tool_css)))
        sel_tol.click()

    def select_continent(self, value):
        self.value = value
        select_t = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.continent_css)))
        dd = Select(select_t)
        dd.select_by_visible_text(self.value)
    def select_command(self, value):
        self.value = value
        select_t = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.selen_comnd_css)))
        dd = Select(select_t)
        dd.select_by_visible_text(self.value)
    def click_image_btn(self):
        click_img_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.img_css)))
        click_img_btn.send_keys("C:/Users/man-s/Downloads/Documents/image.jpg")

    def click_signup_btn(self):
        time.sleep(5)
        click_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Elements.submit_css)))
        click_btn.click()
