#install python3 first
import requests
import os
from bs4 import BeautifulSoup as bs #pip install bs4
import pprint


base_url = "https://octodex.github.com/"


def scrapit(base_url, destination):
    try:
        os.mkdir(destination)
        os.chdir(destination)

    except OSError:
        os.chdir(destination)

    resp = requests.get(base_url)
    soup = bs(resp.text, 'html.parser')

    # Uncomment code below to view the 'soup' object
    # print(soup)


    img = soup.find_all("img")
    links = [x.get('data-src') for x in img]

    img_source = [base_url + x for x in links if x!=None]

    #downloading images

    for link in img_source:
        fname = link.split('/')[-1]

        r = requests.get(link)

        if(os.path.exists(fname)):
            print(fname + " exists")
        else:
            print("Downloading "+ fname)
            with open(fname,'wb') as f:
                f.write(r.content)
