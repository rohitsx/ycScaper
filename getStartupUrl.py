from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os 

with open("html/YC_Startup_Directory.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

s = soup.find('div', class_='_section_1pgsr_163 _results_1pgsr_343')

def getLink():
    urlList = []
    for a in s.find_all('a'): 
        url = a['href']
        urlList.append(url)
    return urlList


if s:
    urlList = getLink()
    csv_name = "startupCsv/urlList-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
    pd.Series(urlList).to_csv(csv_name , index=False)



