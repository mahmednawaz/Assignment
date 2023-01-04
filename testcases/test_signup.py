import time
import pytest
from pages.elements import Elements
from pages.signup import SignUP


@pytest.mark.usefixtures("setup")
class TestSignUp:
    def test_signup_with_valid_credentials(self):
        s_up = SignUP(self.driver)
        s_up.sign_up()