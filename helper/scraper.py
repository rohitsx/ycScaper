from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url):
        self.r = requests.get(url)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')

    def getStartupName(self):
        x =  self.soup.find_all('h1')
        return x[0].text

    def getX(self):
        Xhandle = []
        for a in self.soup.find_all('a', title='Twitter account'):
            Xhandle.append(a['href'])
        return Xhandle

    def getLinkedIn(self):
        LinkedInHandle = []
        for a in self.soup.find_all('a', title='LinkedIn profile'):
            LinkedInHandle.append(a['href'])
        return LinkedInHandle

    def getGithub(self):
        github = self.soup.find_all('a', title='Github profile')
        return github[0]['href']
