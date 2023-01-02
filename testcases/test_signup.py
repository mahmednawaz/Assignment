import time
import pytest
from pages.elements import Elements
from pages.signup import SignUP


@pytest.mark.usefixtures("setup")
class TestSignUp:
    def test_signup(self):
        s_up = SignUP(self.driver, self.wait)
        s_up.fname_textbox(Elements.fname)
        s_up.lname_textbox(Elements.lname)
        s_up.select_gender()
        s_up.select_experience()
        s_up.date_textbox(Elements.date)
        time.sleep(5)
        s_up.select_profession()
        time.sleep(5)
        s_up.select_tool()
        s_up.select_continent(Elements.continent_value)
        s_up.select_command(Elements.selem_comnd_value)
        s_up.click_image_btn()
        s_up.click_signup_btn()
        time.sleep(5)