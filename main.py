from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import *
from data import *
# import pytest

passw = ""
user = ""

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://boxrec.com/en/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID,"password")

username.send_keys(user)
password.send_keys(passw)

driver.find_element(By.NAME,"login[go]").click()

for i in range(286,600):

    url = "https://boxrec.com/en/proboxer/"+str(i)

    info = driver.get(url)

    if "Sorry, we could not find that person" in driver.page_source:
        continue

    d = driver.find_element(By.CLASS_NAME,"profileTable").get_attribute("innerHTML")

    soup = BeautifulSoup(d,'lxml')

    data = []
    tags = ['td.defaultTitleAlign h1']
    for i in tags:
        data.append(extract_data(str(soup.select(i)[0])))

    title =  ['name','wins','loss','draws'] +[extract_data(str(i)) for i in soup.select('td:not(.rowLabel) b')]
    data = data + [extract_data(str(i)) for i in soup.select('table td:not(.rowLabel)')]

    initlization(data,title)

driver.quit()
