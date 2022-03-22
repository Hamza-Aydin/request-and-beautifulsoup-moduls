import requests
from bs4 import BeautifulSoup

url="https://armut.com/g/diger"

a=requests.get(url)

html_içeriği=a.content

b=BeautifulSoup(html_içeriği,"html.parser")
#print(b.prettify())

#print(b.findAll("a")) #sadece link içeren satırları almak istersek

#for i in b.findAll("a"): #<a> etiketlerinin bulunduğu kısımlarda dolaştık
    #print(i)
    #print("*************************************************")

#for i in b.findAll("a"): #sadece linklere ulaştık
    #print(i.get("href"))
    #print("*************************************************")


#for i in b.findAll("a"): #<a> etiketindeki metinlere ulaştık
    #print(i.text)
    #print("*************************************************")

for i in b.findAll("div",{"class":"all-services"}): #class ismi all-services olan bloklara ulaştık
    print(i)
    print("*************************************************")

