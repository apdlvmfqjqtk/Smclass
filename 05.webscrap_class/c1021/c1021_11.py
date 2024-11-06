import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'lxml')
# print(soup)
hott = soup.find("div",{"class":"hot_issue"})
print(hott.find("span",{"class":"title"}).text)
print(hott.find("span",{"class":"ellipsis"}).text)

print(hott.find("a",{"class":"mlog link-thumb"}).src)