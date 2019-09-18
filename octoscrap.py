#install python3 first
import requests
import os
from bs4 import BeautifulSoup as bs #pip install bs4
import pprint

try:
    os.mkdir("Octocats")
    os.chdir("Octocats")

except OSError:
    os.chdir("Octocats")

base_url = "https://octodex.github.com/"



resp = requests.get(base_url)
soup = bs(resp.text, 'html.parser')

img = soup.find_all("img")
links = [x.get('data-src') for x in img]

img_source = [base_url + x for x in links if x!=None]

#downloading images

for link in img_source:
    fname = link.split('/')[-1]

    r = requests.get(link)

    if(os.path.exists(fname)):
        print(f"{fname} exists")
    else:
        print(f"Downloading {fname}")
        with open(fname,'wb') as f:
            f.write(r.content)
