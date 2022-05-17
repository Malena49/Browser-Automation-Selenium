from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("http://demo.seleniumeasy.com/")
driver.implicitly_wait(8)
#at-cm-no-button
Progress_Bars = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Progress Bars")
Progress_Bars.click()
JQuery_Download_Progress_bars = driver.find_element(by=By.LINK_TEXT, value="JQuery Download Progress bars")
JQuery_Download_Progress_bars.click()
downloadButton = driver.find_element(by=By.ID, value="downloadButton")
downloadButton.click()
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
 (By.CLASS_NAME, "progress-label"),  #filtrer 
   "Complete!" # résultat attendu
    )
)