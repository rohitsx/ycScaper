from helper.scraper import Scraper
import pandas as pd 

startupUrl = pd.read_csv('startupCsv/urlList-2025-01-31_22-11-34.csv') #updated this value on new records
socialUrl = []  
for v in startupUrl.items():
    print(v)
