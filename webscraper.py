import pandas as pd
import numpy as np
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

books = []
data = {"genre":[], "title": [], "author": [], "rating": [], "reviews": [], "year": []}
a = 1
for genre in genres:
    page = requests.get(URL + "/" + genre)
    soup = BeautifulSoup(page.content, "html.parser")
    books = soup.findAll(class_="left")
    for book in books:
        title = book.find(class_="bookTitle")
        author = book.find(class_="authorName")
        rating = book.find(class_="greyText smallText")
        ## avg rating 4.45 —\n                26,684 ratings  —\n                published 2011
        rating = rating.text.strip()

        punc = '.,' 
        for ele in rating:
            if ele in punc:
                rating = rating.replace(ele, "")

        numbers = []
        for word in rating.split():
            if word.isdigit():
                numbers.append(int(word))

        numbers[0] = numbers[0]/100
        if (len(numbers) == 3):
            data["genre"].append(genre)
            data["title"].append(title.text)
            data["author"].append(author.text)
            data["rating"].append(numbers[0])
            data["reviews"].append(numbers[1])
            data["year"].append(numbers[2])
        a = a + 1   

df = pd.DataFrame(data)

print(df)
