from django.shortcuts import render
import bs4 as bs
import urllib.request
from urllib.request import Request,urlopen

def tennis(request):

    return render(request,"tennis.html")


def tennis_news(request):
    news=[]
    news1=[]
    time=[]
    about=[]
    sauce=urllib.request.urlopen("http://www.tennis.com/pro-game").read()
    soup=bs.BeautifulSoup(sauce,'html.parser')

    for a1 in soup.find_all('div',class_='news-posts bottom-spacing'):
        for a in a1.find_all('a'):
            b=a.get('href')
            b="https://www.cricbuzz.com/"+b
            b1=a.text
            news.append(b1)
            news1.append(b)
        for a2 in a1.find_all('span',class_='date'):
            time.append(a2.text)
        for a3 in a1.find_all('span',class_='author'):
            about.append(a3.text)

    news=list(map(lambda s: s.strip('\n'),news))
    news1=list(map(lambda s: s.strip('\n'),news1))

    news=list(map(lambda s: s.replace('\n',''),news))
    news1=list(map(lambda s: s.replace('\n',''),news1))

    news=list(filter(None,news))
    news1=list(dict.fromkeys(news1))


    context={'news':news,'news1':news1,'time':time,'r':range(3),'s':range(6),'about':about}
    return render(request,"tennis_news.html",context)

def tennis_mens_rankings(request):
    rank=[]
    anchor=[]
    sauce=urllib.request.urlopen('http://www.tennis.com/rankings/ATP').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    rows=table.find_all('tr')
    head=table.find_all('th')
    rank+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        rank+=[i.text for i in b]
        for c in a.find_all('a'):
            d=c.get('href')
            d="http://www.tennis.com"+d
            anchor+=[d]

    rank=list(map(lambda s: s.strip(),rank))
    context={'rank':rank,'anchor':anchor,'r':range(5,130,5)}
    return render(request,"tennis_mens_rankings.html",context)

def tennis_mens_doubles(request):
    rank=[]
    anchor=[]

    req=Request('https://www.atptour.com/en/rankings/doubles',headers={'User-Agent':'Mozilla/5.0'})
    sauce=urlopen(req).read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    rows=table.find_all('tr')
    head=table.find_all('th')
    rank+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        rank+=[i.text for i in b]
        for c in a.find_all('a'):
            d=c.get('href')
            d="https://www.atptour.com"+d
            anchor+=[d]

    rank=list(map(lambda s: s.strip(),rank))
    anchor=list(dict.fromkeys(anchor))

    anchor=anchor[9::3]
    context={'rank':rank,'anchor':anchor,'r':range(9,500,9)}
    return render(request,"tennis_mens_doubles.html",context)



def tennis_womens_doubles(request):
    rank=[]
    anchor=[]

    req=Request('https://www.tennisexplorer.com/ranking/wta-women/?t=doubles',headers={'User-Agent':'Mozilla/5.0'})
    sauce=urlopen(req).read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    rows=table.find_all('tr')
    head=table.find_all('th')
    rank+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        rank+=[i.text for i in b]
        for c in a.find_all('a'):
            d=c.get('href')
            d="https://www.atptour.com"+d
            anchor+=[d]

    context={'rank':rank,'anchor':anchor,'r':range(9,500,9)}
    return render(request,"tennis_womens_doubles.html",context)


def tennis_womens_rankings(request):
    rank=[]
    anchor=[]
    sauce=urllib.request.urlopen('http://www.tennis.com/rankings/WTA/').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    rows=table.find_all('tr')
    head=table.find_all('th')
    rank+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        rank+=[i.text for i in b]
        for c in a.find_all('a'):
            d=c.get('href')
            d="http://www.tennis.com"+d
            anchor+=[d]

    rank=list(map(lambda s: s.strip(),rank))
    context={'rank':rank,'anchor':anchor,'r':range(5,130,5)}
    return render(request,"tennis_womens_rankings.html",context)
