from cgitb import text
from lib2to3.pgen2 import driver
import string
from typing import Type
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\braya\\Downloads\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get('https://www.bible.com/es/bible/103/HEB.9.NBLA')

#Click in next arrow
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chapter')))
capitulo = driver.find_element(By.CSS_SELECTOR,'div.chapter')
versiculos = capitulo.find_elements(By.CSS_SELECTOR,'span.verse')
for verso in versiculos:
    vv = verso.get_attribute('innerHTML')
    soup = BeautifulSoup(vv, 'html.parser')
    numerovv = soup.find_all('span',None)[0].text
    if re.findall('[0-9]+', numerovv) != []:
        print(numerovv)
    versoArray = soup.select('span.content', None)
    versoTxt=''
    for v in versoArray:
        versoTxt += v.text
    print(versoTxt)
    print('*'*5)

## Recorrer toda la biblia
# nextArrow = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.next-arrow')))
# while nextArrow:
#   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()
