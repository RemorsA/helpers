from bs4 import BeautifulSoup
import requests as req
import os
clear = lambda: os.system('cls')
clear()

# div
# class
# toponym-card-title-view__coords-badge

def parseHtmlPage():
    url = input("Укажите url -> ")
    tag = input("Укажите тег -> ")
    attribute = input('Укажите аттрибут -> ')
    name = input("Укажите класс или id тега -> ")

    resp = req.get(url)

    soup = BeautifulSoup(resp.text, 'lxml')
    cords = soup.find(
        tag,
        attrs={
            attribute : name
        }
    ).text

    print('Ответ ==> ', cords)


parseHtmlPage()