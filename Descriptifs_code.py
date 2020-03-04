# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup, BeautifulSoup
import pandas as pd
import xlrd
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept-Language': 'fr-FR,en;q=0.8'}
df = xlrd.open_workbook("CLEANED_JOB_ADS_INDEED.xlsx")
sheet = df.sheet_by_index(0)
url = []
jobid = []
for i in range(1, 2550):
    url.append(sheet.cell_value(i, 7))
    jobid.append(sheet.cell_value(i, 1))

for i in range(1, 2550):
    unisens = []
    sentences = []
    descriptif = ""
    req = urllib.request.Request(url[i], headers=hdr)
    try:
        urlopen(req)
    except:
        pass
    webpage = urllib.request.urlopen(req).read()
    # Parse the container of the job description using beautifulsoup
    page_soup = soup(webpage, 'html.parser')
    container = page_soup.findAll("div", "jobsearch-jobDescriptionText")
    # Structure the container using text formatting techniques
    descriptif = str(container[0])
    clean_descriptif = descriptif.replace('<p>', '').replace('<b>', '').replace('</p>', '').replace('</b>', '').replace(
        '<br/>', '').replace('</br>', '').replace('<i>', '').replace('<h2>', '').replace('<div>', '').replace('</div>',
                                                                                                          '').replace(
        '</h2>', '').replace('</i>', '').replace('<li>', '').replace('</li>', '').replace('<ul>', '').replace('</ul>',
                                                                                                          '').replace(
        '<h3>', '').replace('</h3>', '').replace('<h4>', '').replace('</h4>', '').replace('</h5>', '').replace('<h5>', '')
    sentences = clean_descriptif.split("<p> . , ; \n")

    f = open("./DESCRIPTION/" + jobid[i] + ".txt", "w", encoding='utf-8')

    for j in sentences:
        f.writelines(j)
f.close()