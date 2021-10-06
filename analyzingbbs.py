import pandas as pd
import numpy as np
import grequests
from bs4 import BeautifulSoup
import csv

df = pd.read_csv("/Users/benjamingoldblatt/webscraper/bestbooks.csv")
books = df['0'].tolist()


reqs = (grequests.get(link) for link in books)
resp = grequests.map(reqs, size=10)

data = {"genre":[], "title": [], "author": [], "rating": [], "reviews": [], "year": [], "description":[], "pages": []}
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
    reviews = soup.find('span',attrs={"itemprop":"ratingCount"})
    if title and genre and rating and authors:
        data["authors"].append(names)
        data["title"].append(title.text.strip())
        data["genre"].append(genre.text)
        data["rating"].append(rating.text.strip())
        data["reviews"].append(rating.text.strip())
    print(data)
print(len(data["rating"]))


