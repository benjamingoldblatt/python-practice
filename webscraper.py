from bs4 import BeautifulSoup
import requests

URL = "https://www.goodreads.com/shelf/show"
num = 1

HOME = "https://www.goodreads.com"

genres = []
page = requests.get(HOME)
soup = BeautifulSoup(page.content, "html.parser")
gs = soup.findAll(class_="gr-hyperlink")
for g in gs:
    genres.append(g.text)


a = 1
for genre in genres:
    page = requests.get(URL + "/" + genre)
    soup = BeautifulSoup(page.content, "html.parser")
    books = soup.findAll(class_="left")
    for book in books:
        title = book.find(class_="bookTitle")
        author = book.find(class_="authorName")
        print (a, title.text + " by " + author.text + "\n")
        a = a + 1   
