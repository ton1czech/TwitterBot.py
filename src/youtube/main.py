from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A/videos")

driver = driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]")
driver.click()