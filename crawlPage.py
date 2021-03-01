# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
from re import search
from goose3 import Goose
from requests.exceptions import ConnectionError, InvalidURL

g = Goose()

liste =  ["twitter.","instagram.","t.me","discord.","youtube.",".html","footer","index.php","login","profile","page","comment","item",
"page","=get","contact","register","advertisement","search","discover"]

def crawLink(site):
    page_number = 0
    control = 0
    with open('wordlist.txt', 'w') as the_file:
        while control != 5:
            page_number = page_number + 1
            url = site + str(page_number)
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            review = []
            control = control + 1
            for i in soup.find_all('a', href=True):
                if search('https://', i['href']):
                    if not any(x in i['href'] for x in liste):
                        try:
                            content = g.extract(url=i['href'])
                            if not ('https://' + content.domain)==content.final_url:
                                link = i['href']
                                the_file.write(f"{link}\n")
                                print(i['href'])
                        except(ConnectionError, InvalidURL):   
                                print('')
            review.append(i)

with open('urlWordlist.txt', 'r+', encoding='utf-8') as urL:
    for site in urL:
        site = site + '?page='
        crawLink(site)