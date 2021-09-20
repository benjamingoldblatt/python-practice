import requests
from bs4 import BeautifulSoup

URL = "https://www.goodreads.com/shelf/show/philosophy"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

titles = soup.findAll(class_="bookTitle")
authors = soup.findAll(class_="authorName")


for title in titles:
    print(title.text)

for author in authors:
    print(author.text)