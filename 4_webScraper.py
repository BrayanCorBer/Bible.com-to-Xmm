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

nbla = ''

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\braya\\Downloads\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get('https://www.bible.com/es/bible/103/GEN.1.NBLA')

#Click in next arrow
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()

# Recorrer toda la biblia
nextArrow = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.next-arrow')))

bookChecker = 'Génesis'
while nextArrow:
    ## Get Book Name
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.reader')))
    bookContainer = driver.find_element(By.CSS_SELECTOR, 'div.reader')
    bookTxt = bookContainer.get_attribute('innerHTML')
    bookSoup = BeautifulSoup(bookTxt,'html.parser')
    bookName = bookSoup.find_all('h1')[0].string
    bookArray = bookName.split(' ')
    bookArray.pop(-1)
    book = ''
    for b in bookArray:
        book = book+b+' '
    
    if bookChecker != book:
        print('</b>')
        print('<b n="'+book[:-1]+'">')
        bookChecker = book

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chapter')))
        capitulo = driver.find_element(By.CSS_SELECTOR,'div.chapter')

        # Get Chap Number
        capTxt = capitulo.get_attribute('innerHTML')
        soup = BeautifulSoup(capTxt, 'html.parser')
        capNum = soup.find_all('div')[0].string
        print('<c n="'+capNum+'">')

        # Get Verses with number

        versiculos = capitulo.find_elements(By.CSS_SELECTOR,'span.verse')

        for verso in versiculos:
            vv = verso.get_attribute('innerHTML')
            soup = BeautifulSoup(vv, 'html.parser')
            numerovv = soup.find_all('span',None)[0].text
            if re.findall('[0-9]+', numerovv) != []:
                print('<v n="'+numerovv+'">')
            versoArray = soup.select('span.content', None)
            versoTxt=''
            for v in versoArray:
                versoTxt += v.text
            print(versoTxt)
            print('</v>')
        print("</c>")

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chapter')))
        capitulo = driver.find_element(By.CSS_SELECTOR,'div.chapter')

        # Get Chap Number
        capTxt = capitulo.get_attribute('innerHTML')
        soup = BeautifulSoup(capTxt, 'html.parser')
        capNum = soup.find_all('div')[0].string
        print('<c n="'+capNum+'">')

        # Get Verses with number

        versiculos = capitulo.find_elements(By.CSS_SELECTOR,'span.verse')

        for verso in versiculos:
            vv = verso.get_attribute('innerHTML')
            soup = BeautifulSoup(vv, 'html.parser')
            numerovv = soup.find_all('span',None)[0].text
            if re.findall('[0-9]+', numerovv) != []:
                print('<v n="'+numerovv+'">')
            versoArray = soup.select('span.content', None)
            versoTxt=''
            for v in versoArray:
                versoTxt += v.text
            print(versoTxt)
            print('</v>')
        print("</c>")

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()



# # Recorrer toda la biblia
# nextArrow = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.next-arrow')))
# while nextArrow:
#   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()
