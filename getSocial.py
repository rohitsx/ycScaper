from helper.scraper import Scraper
import pandas as pd
import json
import datetime

# Read CSV without header to ensure correct URL loading
your_new_create_url_csv = 'startupCsv/urlList-2025-01-31_22-11-34.csv' 
startupUrl = pd.read_csv(your_new_create_url_csv, header=None)

socialUrl = {}

# Iterate over the first column of URLs
for url in startupUrl.iloc[:, 0]:
    try:
        s = Scraper(url)
        linkedin = s.getLinkedIn()  
        name = s.getStartupName()
        x = s.getX()
        try:
            github = s.getGithub()
        except:
            github = None


        if name not in socialUrl:
            socialUrl[name] = {'github': github, 'linkedin': linkedin, 'x': x}
            print(socialUrl[name])


    except Exception as e:
        print(f"Error processing {url}: {e}")  


json_name= "socialJson/Url-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
with open(json_name, 'w', encoding='utf-8') as f:
    json.dump(socialUrl, f, indent=4, ensure_ascii=False)
