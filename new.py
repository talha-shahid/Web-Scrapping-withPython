from itertools import count
from bs4 import BeautifulSoup
import requests



source = requests.get('https://medium.com/').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())


article = soup.find_all('div',class_='ae cx')
count=6
try:
    for item in article:
        # print(count)
        title=article[count].h2.text
        print(title)

        description=article[count].h3.text
        print(description)

        author= article[count].h4.text
        print(author)
        print()
        count=count+1
except:
    pass