from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/python")
driver.implicitly_wait(8)
#my_element = driver.find_element_by_link_text("Run tests in parallel with pytest")
my_element = driver.find_element(by=By.LINK_TEXT, value="Run tests in parallel with pytest")
my_element.click()
