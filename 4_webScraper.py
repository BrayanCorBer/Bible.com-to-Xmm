from typing import Type
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from asyncore import write
from cgitb import text
from asyncore import write
import codecs
from lib2to3.pgen2 import driver
import string

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
import codecs


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



nblaArray = []

bookChecker = 'Génesis'
while True:
    fileB = codecs.open('bible-NBLA.txt', 'a', 'utf-16-le')
    nbla = ''


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
        nbla = nbla + '  </BIBLEBOOK>\r\n'
        nbla = nbla +  '  <BIBLEBOOK bname="'+book[:-1]+'">\r\n'
        bookChecker = book

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chapter')))
        capitulo = driver.find_element(By.CSS_SELECTOR,'div.chapter')

        # Get Chap Number
        capTxt = capitulo.get_attribute('innerHTML')
        soup = BeautifulSoup(capTxt, 'html.parser')
        capNum = soup.find_all('div')[0].string
        nbla = nbla + '    <CHAPTER cnumber="'+capNum+'">\r\n'

        # Get Verses with number

        versiculos = capitulo.find_elements(By.CSS_SELECTOR,'span.verse')

        for verso in versiculos:
            vv = verso.get_attribute('innerHTML')
            soup = BeautifulSoup(vv, 'html.parser')
            numerovv = soup.find_all('span',None)[0].text
            if re.findall('[0-9]+', numerovv) != []:
                nbla = nbla + '<VERS vnumber="'+numerovv+'">'
            versoArray = soup.select('span.content', None)
            versoTxt=''
            for v in versoArray:
                versoTxt += v.text

            if re.findall('[a-z]+',versoTxt) != []:
                nbla = nbla + versoTxt + '</VERS>'
            
        nbla = nbla + "\r\n    </CHAPTER>\r\n"
        nbla2 = re.sub('</VERS>\S','',nbla)
        nbla2 = re.sub('</VERS> ',' ',nbla)
        nbla = re.sub('<VERS','\r\n      <VERS',nbla2)
        nbla2 = re.sub('</VERS>\S','',nbla)
        fileB.write(nbla2)

        #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chapter')))
        capitulo = driver.find_element(By.CSS_SELECTOR,'div.chapter')

        # Get Chap Number
        capTxt = capitulo.get_attribute('innerHTML')
        soup = BeautifulSoup(capTxt, 'html.parser')
        capNum = soup.find_all('div')[0].string
        nbla = nbla + '    <CHAPTER cnumber="'+capNum+'">\r\n'

        # Get Verses with number

        versiculos = capitulo.find_elements(By.CSS_SELECTOR,'span.verse')

        for verso in versiculos:
            vv = verso.get_attribute('innerHTML')
            soup = BeautifulSoup(vv, 'html.parser')
            numerovv = soup.find_all('span',None)[0].text
            if re.findall('[0-9]+', numerovv) != []:
                nbla = nbla + '<VERS vnumber="'+numerovv+'">'
            versoArray = soup.select('span.content', None)
            versoTxt=''
            for v in versoArray:
                versoTxt += v.text
            #print(versoTxt)
            if re.findall('[a-z]+',versoTxt) != []:
                nbla = nbla + versoTxt + '</VERS>'
            
        nbla = nbla + "\r\n    </CHAPTER>\r\n"
        nbla2 = re.sub('</VERS>\S','',nbla)
        nbla2 = re.sub('</VERS> ',' ',nbla)
        nbla = re.sub('<VERS','\r\n      <VERS',nbla2)
        nbla2 = re.sub('</VERS>\S','',nbla)
        fileB.write(nbla2)

    
    
    fileB.close()
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()
    except:
        break

# fileB = open('bible.txt', 'a')
# for b in nblaArray:
#     fileB.write(b)
# fileB.close() 



# # Recorrer toda la biblia
# nextArrow = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.next-arrow')))
# while nextArrow:
#   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.next-arrow'))).click()
