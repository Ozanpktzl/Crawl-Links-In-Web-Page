from goose3 import Goose 
from requests.exceptions import MissingSchema, InvalidURL, ConnectionError
import csv
import time

g = Goose()
config = {}
config['strict'] = False
config['browser_user_agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
config['https_timeout'] = 5.05

urls=open("wordlist.txt","r",encoding="utf-8")
with Goose() as g:
    with open('content.csv', mode='+w') as content_file:
        content_writer = csv.writer(content_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        content_writer.writerow(['domain','url','title', 'content'])
        for tmp in urls:
            try: 
                content=g.extract(url=tmp)                
                content_writer.writerow([content.domain, content.final_url,content.title, content.cleaned_text])
                time.sleep(0.5)
                print("hooop content")
            except(MissingSchema, InvalidURL, ConnectionError):
                pass
        

g.close()