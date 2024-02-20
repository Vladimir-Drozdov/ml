from bs4 import BeautifulSoup
import requests
import lxml
#url = 'http://mignews.com/mobile'
url='https://salons-tet.ru/'
page = requests.get(url)
#print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
#print(all_text.text)
title=soup.title

#Методы find и find_all()
page_h1=soup.find_all(class_="price_list")[0].find("div", {"class":"a"})

#print(page_h1.get("class"))
map = soup.find("div", {"id":"map"})
#print(map.find_parents("div"))
el=soup.find("div", class_="contacts_and_map")
print(el.find_next()["class"])
elemtext=soup.find("div", string="г. Петрозаводск, ул. Максима Горького, д. 24")
print(elemtext.text.split())
with open('cosmetics.html', 'r', encoding="utf8") as html: #r-read, w-write
    content = html.read()
    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify())

#requests

API_TOKEN = "ddd23e3aea33b0c280a82a4a81c0cd46"
params = {"q": "Лондон", "appid": API_TOKEN}
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
print(response.json()["weather"][0]['main'])
print(response.headers)
#POST
headers={
    "Accept":"application/json"
}
data={
    "custname":"логин",
    "custtel":"6563738",
    "size":"medium"
}
response=requests.post("https://httpbin.org/post", headers=headers, data=data)
print(response.json())

print(response.status_code)
variable=requests.Session()
aaa=variable.get("https://httpbin.org/form/post")
print("aaa ",aaa)