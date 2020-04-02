import requests
import urllib.request
import time
import bs4 as bs
import pandas as pd

##row=[]
##sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').read()
##soup=bs.BeautifulSoup(sauce,'html.parser')
##table=soup.table
##rows=table.find_all('tr')
##update=soup.find('div',class_='rankings-table__last-updated')
##print(update.text)
##
##news=[]
##news1=[]
##sauce=urllib.request.urlopen('https://www.cricbuzz.com/').read()
##soup=bs.BeautifulSoup(sauce,'html.parser')
##col=soup.find('div',class_='cb-col-47')
##for a in col.find_all('a'):
##    b=a.get('href')
##    b1=a.text
##    news.append(b1)
##    news1+=b



sauce=urllib.request.urlopen("http://www.tennis.com/pro-game").read()
soup=bs.BeautifulSoup(sauce,'html.parser')

a1=[]
a=soup.find_all('div',class_='news-posts')
print(a)



##
##
##sauce=urllib.request.urlopen('http://www.tennis.com/rankings/ATP').read()
##soup=bs.BeautifulSoup(sauce,'html.parser')
##table=soup.table
##rows=table.find_all('tr')
##head=table.find_all('th')
##
##for a in rows:
##    b=a.find_all('a')
##    print(b)
    
##sauce1=urllib.request.urlopen('https://www.espncricinfo.com/').read()
##soup1=bs.BeautifulSoup(sauce1,'html.parser')
##news2=[]
##
##news3=[]
##
##for a1 in soup1.find_all('ul',class_='headlineStack_list'):
##    for a in a1.find_all('a'):
##        print(a.get('href'))
##        b="https://www.espncricinfo.com/"+b
##        b1=a.text
##        news2.append(b1)
##        news3.append(b)
##
##
##print(news2)
##print(news3)



##for a in rows:
##    b=a.find_all('td')
##    row+=[i.text for i in b]
##print(row)
##sauce=urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
##soup=bs.BeautifulSoup(sauce,'html.parser')
##
##
##for i in soup.find_all('loc'):
##    print(i.text)

##sauce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
##soup=bs.BeautifulSoup(sauce,'html.parser')
##
##
##print(soup.title.string)
##
##print(soup.find_all('p'))
##
##soup.get_text()
##
##for para in soup.find_all('p'):
##    print(para.text)
##
##for url in soup.find_all('a'):
##    print(url.get('href'))
##
##nav = soup.nav
##
##for a in nav.find_all('a'):
##    print(a)
##for div in soup.find_all('div',class_='body'):
##    print(div.text)
##
##table=soup.table
##table_r=table.find_all('tr')
##
##for tr in table_r:
##    td=tr.find_all('td')
##    row=[i.text for i in td]
##    print(row)
##
