import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://google.com')

googleSearchBox = driver.find_element(By.ID,"APjFqb")
googleSearchBox.send_keys("Aaron Daniel Chiemezie")
googleSearchBox.send_keys(Keys.RETURN)
# driver.get("https://trytestingthis.netlify.app/")
# driver.find_element(By.ID, "fname").send_keys("Daniel Chiemezie")
# driver.find_element(By.ID, "lname").send_keys("Aaron")
# driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5)
driver.close()
driver.quit()