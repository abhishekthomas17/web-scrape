from django.shortcuts import render
import bs4 as bs
import urllib.request
from urllib.request import Request,urlopen


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def sports(request):
    return render(request,"sports.html")

def cricket(request):
    return render(request,"cricket_mens.html")

def cricket_news(request):
    news=[]
    news1=[]
    time=[]
    about=[]
    news3=[]
    news2=[]


    req = Request('https://www.cricbuzz.com/cricket-news/latest-news', headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urlopen(req).read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    sauce1=urllib.request.urlopen('https://www.espncricinfo.com/').read()
    soup1=bs.BeautifulSoup(sauce1,'html.parser')

    for a1 in soup.find_all('div',class_='cb-lst-itm'):
        for a in a1.find_all('a'):
            b=a.get('href')
            b="https://www.cricbuzz.com/"+b
            b1=a.text
            news.append(b1)
            news1.append(b)
        for a2 in a1.find_all('span',class_='cb-nws-time'):
            time.append(a2.text)
        for a3 in a1.find_all('div',class_='cb-nws-time'):
            about.append(a3.text)
    col=soup1.find('section',class_='col-three')
    for a1 in col.find_all('ul',class_='headlineStack__list'):
        for a in a1.find_all('a'):
            b=a.get('href')
            b="https://www.espncricinfo.com"+b
            b1=a.text
            news2.append(b1)
            news3.append(b)
    news=list(filter(None,news))
    news1=list(dict.fromkeys(news1))


    context={'news':news,'news1':news1,'news2':news2,'news3':news3,'time':time,'r':range(10),'s':range(6),'about':about}
    return render(request,"cricket_news.html",context)
def mens_odi(request):
    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-table__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))
    # roww=''.join(row)
    context={'icc':row,'r':range(5,90,5),'date':update.text}
    return render(request,"mens_odi.html",context)

def player_ranking_odi(request):
    row=[]
    row1=[]
    row2=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting').read()
    sauce1=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling').read()
    sauce2=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder').read()
    soup2=bs.BeautifulSoup(sauce2,'html.parser')
    soup=bs.BeautifulSoup(sauce,'html.parser')
    soup1=bs.BeautifulSoup(sauce1,'html.parser')


    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    table1=soup1.table
    update1=soup1.find('div',class_='rankings-block__last-updated')
    rows1=table1.find_all('tr')
    head1=table1.find_all('th')
    row1+=[i.text for i in head1]
    for a1 in rows1:
        b1=a1.find_all('td')
        row1+=[i.text for i in b1]
    row1=list(map(lambda s: s.strip(),row1))

    table2=soup2.table
    update2=soup2.find('div',class_='rankings-block__last-updated')
    rows2=table2.find_all('tr')
    head2=table2.find_all('th')
    row2+=[i.text for i in head2]
    for a2 in rows2:
        b2=a2.find_all('td')
        row2+=[i.text for i in b2]
    row2=list(map(lambda s: s.strip(),row2))


    context={'icc':row,'icc1':row1,'icc2':row2,'r':range(4,25,4),'date':update.text,'date1':update1.text,'date2':update1.text,'team':'Team','dash':'--'}
    return render(request,"player_ranking_odi.html",context)


def player_ranking_odi_batting(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_odi_batting.html",context)

def player_ranking_odi_bowling(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_odi_bowling.html",context)


def player_ranking_odi_all_rounder(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_odi_all_rounder.html",context)

def mens_test(request):
    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/team-rankings/test').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-table__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))
    # roww=''.join(row)
    context={'icc':row,'r':range(5,55,5),'date':update.text}
    return render(request,"mens_test.html",context)


def player_ranking_test(request):
    row=[]
    row1=[]
    row2=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/test/batting').read()
    sauce1=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/test/bowling').read()
    sauce2=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/test/all-rounder').read()
    soup2=bs.BeautifulSoup(sauce2,'html.parser')
    soup=bs.BeautifulSoup(sauce,'html.parser')
    soup1=bs.BeautifulSoup(sauce1,'html.parser')


    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    table1=soup1.table
    update1=soup1.find('div',class_='rankings-block__last-updated')
    rows1=table1.find_all('tr')
    head1=table1.find_all('th')
    row1+=[i.text for i in head1]
    for a1 in rows1:
        b1=a1.find_all('td')
        row1+=[i.text for i in b1]
    row1=list(map(lambda s: s.strip(),row1))

    table2=soup2.table
    update2=soup2.find('div',class_='rankings-block__last-updated')
    rows2=table2.find_all('tr')
    head2=table2.find_all('th')
    row2+=[i.text for i in head2]
    for a2 in rows2:
        b2=a2.find_all('td')
        row2+=[i.text for i in b2]
    row2=list(map(lambda s: s.strip(),row2))


    context={'icc':row,'icc1':row1,'icc2':row2,'r':range(4,25,4),'date':update.text,'date1':update1.text,'date2':update1.text,'team':'Team','dash':'--'}
    return render(request,"player_ranking_test.html",context)

def player_ranking_test_batting(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/test/batting').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_test_batting.html",context)


def player_ranking_test_bowling(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/test/bowling').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_test_bowling.html",context)


def player_ranking_test_all_rounder(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/test/all-rounder').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_test_all_rounder.html",context)


def mens_t20(request):
    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/team-rankings/t20i').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-table__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))
    # roww=''.join(row)
    context={'icc':row,'r':range(5,91,5),'date':update.text}
    return render(request,"mens_t20.html",context)


def player_ranking_t20(request):
    row=[]
    row1=[]
    row2=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/batting').read()
    sauce1=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/bowling').read()
    sauce2=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/all-rounder').read()
    soup2=bs.BeautifulSoup(sauce2,'html.parser')
    soup=bs.BeautifulSoup(sauce,'html.parser')
    soup1=bs.BeautifulSoup(sauce1,'html.parser')


    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    table1=soup1.table
    update1=soup1.find('div',class_='rankings-block__last-updated')
    rows1=table1.find_all('tr')
    head1=table1.find_all('th')
    row1+=[i.text for i in head1]
    for a1 in rows1:
        b1=a1.find_all('td')
        row1+=[i.text for i in b1]
    row1=list(map(lambda s: s.strip(),row1))

    table2=soup2.table
    update2=soup2.find('div',class_='rankings-block__last-updated')
    rows2=table2.find_all('tr')
    head2=table2.find_all('th')
    row2+=[i.text for i in head2]
    for a2 in rows2:
        b2=a2.find_all('td')
        row2+=[i.text for i in b2]
    row2=list(map(lambda s: s.strip(),row2))


    context={'icc':row,'icc1':row1,'icc2':row2,'r':range(4,25,4),'date':update.text,'date1':update1.text,'date2':update1.text,'team':'Team','dash':'--'}
    return render(request,"player_ranking_t20.html",context)


def player_ranking_t20_batting(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/batting').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_t20_batting.html",context)

def player_ranking_t20_bowling(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/bowling').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_t20_bowling.html",context)

def player_ranking_t20_all_rounder(request):

    row=[]
    sauce=urllib.request.urlopen('https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/all-rounder').read()
    soup=bs.BeautifulSoup(sauce,'html.parser')
    table=soup.table
    update=soup.find('div',class_='rankings-block__last-updated')
    rows=table.find_all('tr')
    head=table.find_all('th')
    row+=[i.text for i in head]
    for a in rows:
        b=a.find_all('td')
        row+=[i.text for i in b]
    row=list(map(lambda s: s.strip(),row))

    context={'icc':row,'r':range(4,400,4),'date':update.text,'team':'Team','dash':'--'}

    return render(request,"player_ranking_t20_all_rounder.html",context)
