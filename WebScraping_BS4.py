from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame
import urllib.request
import urllib.parse
email = []
firma = []
telefon = []
opis = []
cat = []

url = 'https://www.pkt.pl/szukaj/wrocław/70'
url = urllib.parse.urlsplit(url)
url = list(url)
url[2] = urllib.parse.quote(url[2])
url = urllib.parse.urlunsplit(url)
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"lxml")
comp = soup.find_all("div",class_="box-content company-row list-sel ")
for item in comp:
    e_mail = item.find("div",class_="call-cell call--email")
    if not e_mail:
        email.append("N/A")
    else:
        email.append(e_mail.find("span")["title"])
    nazwa = item.find("h2",class_="company-name")
    if not nazwa:
        firma.append("N/A")
    else:
        firma.append(nazwa.text)
    tele = item.find("div", class_="call-cell call--phone")
    if not tele:
        telefon.append("N/A")
    else:
        telefon.append(tele.find("a")['data-phone'])
    x = item.find("div", class_="company-snippet")
    if not x:
        opis.append("N/A")
    else:
        opis.append(x.text)
    y = item.find("div", class_="company-category")
    if not y:
        cat.append("N/A")
    else:
        cat.append(y.text)
compv1 = soup.find_all("div",class_="box-content company-row ")
for item in compv1:
    e_mail = item.find("div",class_="call-cell call--email")
    if not e_mail:
        email.append("N/A")
    else:
        email.append(e_mail.find("span")["title"])
    nazwa = item.find("h2",class_="company-name")
    if not nazwa:
        firma.append("N/A")
    else:
        firma.append(nazwa.text)
    tele = item.find("div", class_="call-cell call--phone")
    if not tele:
        telefon.append("N/A")
    else:
        telefon.append(tele.find("a")['data-phone'])
    x = item.find("div", class_="company-snippet")
    if not x:
        opis.append("N/A")
    else:
        opis.append(x.text)
    y = item.find("div", class_="company-category")
    if not y:
        cat.append("N/A")
    else:
        cat.append(y.text)
compv2 = soup.find_all("div",class_="box-content company-row list-free")
for item in compv2:
    e_mail = item.find("div",class_="call-cell call--email")
    if not e_mail:
        email.append("N/A")
    else:
        email.append(e_mail.find("span")["title"])
    nazwa = item.find("h2",class_="company-name")
    if not nazwa:
        firma.append("N/A")
    else:
        firma.append(nazwa.text)
    tele = item.find("div", class_="call-cell call--phone")
    if not tele:
        telefon.append("N/A")
    else:
        telefon.append(tele.find("a")['data-phone'])
    x = item.find("div", class_="company-snippet")
    if not x:
        opis.append("N/A")
    else:
        opis.append(x.text)
    y = item.find("div", class_="company-category")
    if not y:
        cat.append("N/A")
    else:
        cat.append(y.text)
firma = Series(firma)
email = Series(email)
telefon = Series(telefon)
opis = Series(opis)
cat = Series(cat)
Baza = pd.concat([firma, cat, opis, telefon, email], axis=1)
Baza.columns = ['Nazwa_Firmy', 'Kategria', 'Opis', 'Telefon', 'Email']
Baza = Baza[Baza.Telefon != "N/A"]
Baza = Baza.drop_duplicates(subset=["Nazwa_Firmy"], keep='first')
Baza = Baza.reset_index(drop=True)
Baza.to_csv('baza_firm.csv', encoding='utf-8')