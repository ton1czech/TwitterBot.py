import os
from os import environ
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.binary_location = environ["GOOGLE_CHROME_PATH"]
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--remote-debugging-port=9222')

def get_youtube_video():
    driver = webdriver.Chrome(executable_path=environ["CHROMEDRIVER_PATH"], chrome_options=options)
    open_browser(driver)

def open_browser(driver):
    global title, link
    title = link = None
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A/videos")

    agreement = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]'))).click()
    video = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]')))
    title = video.text

    read_checker = open('src/youtube/checker.txt', 'r')
    latest_title = read_checker.readline()

    if latest_title == title:
        driver.close()
        title = link = None
        return
    else:
        update_checker = open('src/youtube/checker.txt', 'w')
        update_checker.write(title)

        video.click()
        link = driver.current_url
        driver.close()

get_youtube_video()