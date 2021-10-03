import requests
import config

from bs4 import BeautifulSoup

URL = "https://www.goodreads.com"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
books = soup.findAll(class_="left")

books = []
