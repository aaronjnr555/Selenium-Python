import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password",[
    ("test", "test"),
    ("jonze", "jonze"),
    ("test", "test1")
])


def test_login(driver, username, password):
    driver.get("https://trytestingthis.netlify.app/")
    username_field = driver.find_element(By.ID, "uname")
    password_field = driver.find_element(By.ID, "pwd")
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")


    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(2)
    login_button.click()
    assert 'Success' in driver.page_source
    time.sleep(2)