from bs4 import BeautifulSoup
import requests

url = "https://www.sacnilk.com/articles/internet/instagram/List_of_MostFollowed_Instagram_Handle_in_World?hl=en"
# url = "https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
info = soup.find_all(class_="td")
list_dictionary = []
while info:
    keys = ["number", "name", "followers", "followings", "profession", "country"]
    names = [info[0].text, info[1].text, info[2].text, info[3].text, info[4].text, info[5].text]
    diction = dict(zip(keys, names))
    list_dictionary.append(diction)
    print(diction)
    del info[0:6]




