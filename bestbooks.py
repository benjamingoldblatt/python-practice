import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


BESTBOOKS = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page="
BOOK = "https://www.goodreads.com"

bookurls = []
a = 1
while a < 3:
    page = requests.get(BESTBOOKS + str(a))
    soup = BeautifulSoup(page.content, "html.parser")
    books = soup.findAll("a", class_="bookTitle", href=True)
    for book in books:
        url = book["href"]
        bookurls.append(url)
    a = a+1
print(bookurls)

data = {"genre":[], "title": [], "authors": [], "rating": [], "reviews": [], "year": [], "description": []}

for book in bookurls:
    page = requests.get(BOOK + book)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="bookTitle")
    data["title"].append(title.text)
    authors = soup.findAll(class_="authorName")
    for auth in authors:
        names = []
        names.append(auth.text)
        data["authors"].append(names)
    genre = soup.find(class_="actionLinkLite bookPageGenreLink")
    data["genre"].append(genre)
    rating = soup.find(itemprop="ratingValue")
    data["rating"] = rating.text

print(data)
