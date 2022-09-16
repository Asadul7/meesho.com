from bs4 import BeautifulSoup
from time import sleep
import csv
import requests
total_link=[]
for i in range(1,2):
    url="https://www.jiomart.com/c/beauty/make-up/3102/"+"page/"+ str(i)
    reponses= requests.get(url)
    soup= BeautifulSoup(reponses.content,"html.parser")
    urls=soup.find_all("a",attrs={"class":"category_name prod-name"})
    for element in urls:
        url_link="https://www.jiomart.com"+ element["href"]
        total_link.append(url_link)

for link in total_link:
    responses2= requests.get(link)
    soup2= BeautifulSoup(responses2.content,"html.parser")
    image= soup2.find("div",attrs={"id":"left_col"}).find("div").find("div").find("div").find("img")["data-src"]

    title_name= soup2.find("div",attrs={"class":"title-section"}).text.strip()
    price= soup2.find("span",attrs={"class":"final-price"}).text.strip()


    al_info=[link,image ,title_name ,price]
    f = open('al_info.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(al_info)
    f.close()