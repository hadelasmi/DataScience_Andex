#%%
# -*- coding: utf-8 -*-

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from multiprocessing import Pool
from urllib.parse import urljoin
import requests
import time

df = pd.DataFrame(columns=["Title","Location","Company","Description","URL"])
driver = webdriver.Chrome("./chromedriver_win32/chromedriver")
for i in range(0,100,10):

    driver.get("https://www.indeed.fr/jobs?q=banque&l=paris&start="+str(i))
    #driver.implicitly_wait(2)
    all_jobs = driver.find_elements_by_class_name('result')
    for job in all_jobs:
        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html,'html.parser')
    #print(soup.prettify())
        try:
            title = soup.find("a",class_="jobtitle").text.replace('\n','')
        except:
            title = 'None'
        try:
            location = soup.find(class_="location").text
        except:
            location = 'None'
        try:
            company = soup.find(class_="company").text.replace("\n","").strip()
        except:
            company = 'None'
        try:
            summary = soup.find('div', class_="summary").text.replace("\n","").strip()
        except:
            summary = 'None'
        try:
            txt= ' [" '
            txt1 = ' "] '
            urls = soup.findAll('a',{'rel': 'nofollow', 'target': '_blank'})  # this are the links of the job posts
            urls = ("https://www.indeed.fr"+str([link['href'] for link in urls]).replace("['","").replace("']","").replace(txt,"").replace(txt1,""))
        except:
            urls='None'
        '''try:
            subURL = ""
            #subURL = soup.find('a[onmousedown*="return rclk(this,jobmap["]')
            for adlink in soup.select('a[onmousedown*="return rclk(this,jobmap["]'):
                subURL = "https://www.indeed.fr" + adlink['href']
        except:
            subURL='None' '''
    #sum_div = job.find_elements_by_class_name("summary")
    #sum_div.click()
        df = df.append({'Title':title,'Location':location,"Company":company,"Description":summary,'URL':urls},ignore_index=True)
        df.to_csv(r'C:/Users/lenovo/Desktop/Indeed/BPCE_INDEED.csv',header=True,encoding='utf-8',index=False)













