import pandas as pd
import numpy as np
import grequests
import re
from bs4 import BeautifulSoup
import csv

df = pd.read_csv("/Users/benjamingoldblatt/webscraper/bestbooks.csv")
books = df['0'].tolist()


reqs = (grequests.get(link) for link in books)
resp=grequests.imap(reqs, grequests.Pool(10))


data = {"genres":[], "title": [], "authors": [], "rating": [], "reviews": [], "description":[], "pages": []}
for r in resp:
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.find(id="bookTitle")
    names = []
    genrs = []
    authors = soup.findAll(class_="authorName")
    for auth in authors:
        names.append(auth.text)
    genres = soup.find_all(class_="actionLinkLite bookPageGenreLink", limit=2)
    for genre in genres:
        genrs.append(genre.text)
    rating = soup.find('span',attrs={"itemprop":"ratingValue"})
    pgs = soup.find('span',attrs={"itemprop":"numberOfPages"})
    numratings = soup.find("a", href="#other_reviews")
    description = soup.find(class_='readable stacked')
    if (description):
        description = description.find("span")

    if title and genre and rating and authors and numratings and pgs and description:
        data["authors"].append(names)
        data["title"].append(title.text.strip())
        data["pages"].append(re.sub("[^0-9]", "", pgs.text))
        data["genres"].append(genrs)
        data["rating"].append(rating.text.strip())
        data["description"].append(description.text.strip())
        data["reviews"].append(re.sub("[^0-9]", "", numratings.text))

df = pd.DataFrame(data)
df.to_csv('bestbooksdescr.csv', index=False)