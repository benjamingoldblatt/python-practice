import pandas as pd
import numpy as np
import grequests
from bs4 import BeautifulSoup
import requests


BESTBOOKS = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page="
BOOK = "https://www.goodreads.com"

bookurls = []
data = {"genre":[], "title": [], "authors": [], "rating": [], "reviews": [], "year": [], "description": []}

a = 1
while a < 2:
    page = requests.get(BESTBOOKS + str(a))
    soup = BeautifulSoup(page.content, "html.parser")
    books = soup.findAll("a", class_="bookTitle", href=True)
    for book in books:
        url = book["href"]
        bookurls.append("https://www.goodreads.com" + url)
    a = a+1
df = pd.DataFrame(bookurls)
df.to_csv('bestbooks.csv', index=False)

reqs = (grequests.get(link) for link in bookurls)
resp = grequests.map(reqs, size=40)

for r in resp:
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find(id="bookTitle")
    names = []
    authors = soup.findAll(class_="authorName")
    for auth in authors:
        names.append(auth.text)
    print(names)
    genre = soup.find(class_="actionLinkLite bookPageGenreLink")
    rating = soup.find('span',attrs={"itemprop":"ratingValue"})
    if title and genre and rating and authors:
        data["authors"].append(names)
        data["title"].append(title.text.strip())
        data["genre"].append(genre.text)
        data["rating"].append(rating.text.strip())
    print(data)
print(len(data["rating"]))


