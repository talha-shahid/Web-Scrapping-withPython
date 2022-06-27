
from bs4 import BeautifulSoup
import requests



source = requests.get('https://medium.com/').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())


article = soup.find_all('div',class_='ae cx')
counting=6
try:
    for item in article:
        # print(count)
        title=article[counting].h2.text
        print(title)

        description=article[counting].h3.text
        print(description)

        author= article[counting].h4.text
        print(author)
        print()
        counting=counting+1
except:
    pass