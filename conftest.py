from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.elements import Elements
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get(Elements.link)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    # driver.close()
