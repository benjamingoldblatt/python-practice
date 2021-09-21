import requests
from bs4 import BeautifulSoup

URL = "https://www.goodreads.com/shelf/show/philosophy"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
books = soup.findAll(class_="left")

a = 1
for book in books:
    title = book.find(class_="bookTitle")
    author = book.find(class_="authorName")
    print (a, title.text + " by " + author.text + "\n")
    a = a + 1
