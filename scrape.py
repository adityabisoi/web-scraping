import requests
from bs4 import BeautifulSoup
import pprint

page=requests.get('https://news.ycombinator.com/news')
soup=BeautifulSoup(page.text,'html.parser')
links = soup.select('.storylink')
points=soup.select('.score')
def sorted_list(hnsort):
    return sorted(hnsort,key = lambda k:k['points'],reverse = True)
def custom_links(links,points):
    hn = []
    for i,content in enumerate(links):
        title=links[i].getText()
        href=links[i].get('href')
        votes=int(points[i].getText().replace(' points',''))
        if votes>100:
            hn.append({'title':title,'link':href, 'points':votes})
    return sorted_list(hn)
pprint.pprint(custom_links(links,points))