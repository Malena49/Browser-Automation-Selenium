from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.seleniumeasy.com/python")
driver.implicitly_wait(8)
#my_element = driver.find_element_by_link_text("Run tests in parallel with pytest")
my_element = driver.find_element(by=By.LINK_TEXT, value="Run tests in parallel with pytest")
my_element.click()
