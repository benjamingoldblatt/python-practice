import pandas as pd
import numpy as np
import grequests
from bs4 import BeautifulSoup
import requests


BESTBOOKS = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page="
BOOK = "https://www.goodreads.com"

bookurls = []
a = 1
while a < 30:
    page = requests.get(BESTBOOKS + str(a))
    soup = BeautifulSoup(page.content, "html.parser")
    books = soup.findAll("a", class_="bookTitle", href=True)
    for book in books:
        url = book["href"]
        bookurls.append("https://www.goodreads.com" + url)
    a = a+1
df = pd.DataFrame(bookurls)
df.to_csv('bestbooks.csv', index=False)


