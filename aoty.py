#import libraries
import urllib2
from bs4 import BeautifulSoup
from random import *
quote_page = 'http://www.albumoftheyear.org/ratings/user-highest-rated/'
year = ""
while(year>2017):
    year = input("Year or Decade: ")
isDecade = False
if(year%10==0):
    askDecade = raw_input("The decade?(y/n: )")
    if(askDecade=="Y"):
        isDecade=True

quote_page +=str(year)
if(isDecade):
    quote_page = quote_page + "s/"
else:
    quote_page = quote_page + "/"
index = randint(1,101)
page_number = int(index/20)+1
real_page =quote_page + str(page_number) + "/"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(real_page, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

soup = BeautifulSoup(page,'html.parser')
name_box = soup.find_all('span', attrs={'itemprop': 'itemListElement'})
while(not name_box):
    index = randint(1,index)
    page_number = int(index/20)+1
    real_page =quote_page + str(page_number) + "/"
    req = urllib2.Request(real_page, headers=hdr)

    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    
    soup = BeautifulSoup(page,'html.parser')
    name_box = soup.find_all('span', attrs={'itemprop': 'itemListElement'})
for x in name_box:
    if((str(index)+". ") in x):
        print(x.get_text())
