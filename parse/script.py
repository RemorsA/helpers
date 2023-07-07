from bs4 import BeautifulSoup
import requests as req
import json
import os
import os.path
clear = lambda: os.system('cls')
clear()

def writeToJson(outsideFile, img, width, height, elements):
    if (os.path.exists(outsideFile) == False):
        json.dump({"data": []}, open(outsideFile, 'a'))

    openFile = json.load(open(outsideFile))

    openFile['data'].append({
        "image": img,
        "imageWidth": width,
        "imageHeight": height,
        "elements": elements
    })

    json.dump(openFile, open(outsideFile, 'w'))

# 'https://www.autoopt.ru/auto/catalog/engine/komatsu/saa4d107e_1a_2898/9?view=details-bottom'
def parsePage():
    url = input('URL')
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    html = soup.find('div', attrs={ 'id' : 'Image' })

    style = html['style'].split()
    width = style[0][+6:]
    height = style[1][+7:]

    image = 'https://www.autoopt.ru/' + html.findChildren('img', recursive=False)[0]['src']

    childDiv = html.findChildren('div', recursive=False)

    splitElements = []

    for child in childDiv:
        splitElements.append(child['style'])

        # for i in child['style'].split(';'):

        #     if i != "":
                # splitElements.append(i.lstrip())
            #     newValue = i.lstrip().split(': ')

            #     print(newValue)

                # if (newValue[0] != '' or newValue[1] != ''):
                #     key = newValue[0].lstrip()
                #     value = newValue[1].lstrip()

                    # splitElements.append({ key: value })

    writeToJson('data.json', image, width, height, splitElements)

parsePage()