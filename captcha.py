import selenium
import matplotlib.pyplot as plt
import cv2
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import os

driver = webdriver.Chrome(
    r'D:\chromedriver\chromedriver_win32_3\chromedriver.exe')

url = "https://evisaforms.state.gov/default.asp?CSRFToken=749583751CDE4E3081C36AA7377E67CE&PostCode=ERB&CountryCode=IRAQ++++++&CountryCodeShow=&PostCodeShow=&Submit=Submit"
driver.get(url)
sleep(5)
refresh_id = "frmconinput_ReloadLink"
refresh = driver.find_element_by_id(refresh_id)
i = 0
N = 256


pbar = tqdm(total=N)
while i < N:
    try:
        filename = f'captcha_{167}_{i}.jpg'
        filename2 = f'captcha_{167}_{i}.jpg'

        img = driver.find_element_by_id("frmconinput_CaptchaImage")
        img2 = driver.find_element_by_id("frmconinput2_CaptchaImage")

        if os.path.exists(filename, filename2):
            print(f'Passing image {filename, filename2}...')
            i += 1
            pbar.update(1)
            continue
        with open(filename, 'wb') as file:
            file.write(img.screenshot_as_png)
        refresh.click()
        i += 1
        pbar.update(1)
        sleep(5)
    except:
        print('Something went wrong. Retrying...')
        refresh.click()
        sleep(5)
pbar.close()
driver.close()
