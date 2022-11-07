import requests 
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd     
import cloudscraper
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time


keywords = ["computer+science", "java developer", "coder", "programmer","c++ developer"]
locations = ["Amsterdam"]
types = ["internship"]
languages = ["en"]
job_url = list()
job_names = list()
scraper = cloudscraper.create_scraper(delay=0.5, browser='chrome')
main_url ="https://nl.indeed.com/jobs?q=computer+science&l=Amsterdam&sc=0kf%3Ajt%28internship%29%3B&lang=en&redirected=1&vjk=fc626af05d9a5b7b"

driver = webdriver.Chrome()

df = pd.DataFrame()

driver.get(main_url)

#links = driver.find_elements(By.XPATH,"//li/a")

links = driver.find_elements(By.XPATH,"//li/h2")
for li in links:

        job_url.append(li.get_attribute('href'))

for jobs in job_url:
    r = (scraper.get(jobs)).text
    soup=BeautifulSoup(r, features = "html.parser")
    anan = soup.find('span',{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded"})
    print(anan)


driver.quit()
