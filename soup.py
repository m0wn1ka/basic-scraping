import requests
import csv
from bs4 import BeautifulSoup as bs
import csv
a="""            ___                __ _         
            / _ \              /_ | |        
  _ __ ___ | | | |_      ___ __ | | | ____ _ 
 | '_ ` _ \| | | \ \ /\ / / '_ \| | |/ / _` |
 | | | | | | |_| |\ V  V /| | | | |   < (_| |
 |_| |_| |_|\___/  \_/\_/ |_| |_|_|_|\_\__,_|
"""
print(a)
URL='https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r = requests.get(URL)

soup = bs(r.text, 'html.parser')
titles = soup.find_all('div',class_="_30jeq3 _1_WHN1")
names=soup.find_all('div',class_="_4rR01T")
titles_list = []
count = 1
for title in titles:
    count += 1
    x=title.text
    titles_list.append(x)
tlist=[]     
res=[]   
c=1
for t in names:
    c=c+1
    y=t.text
    tlist.append(y)
for i in range(len(tlist)):
    concatenated_sublist = tlist[i] + titles_list[i]
    # adding the concatenated sublist to the result list
    res.append(concatenated_sublist)
for i in res:
    print(i)
                 
