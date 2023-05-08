from bs4 import BeautifulSoup
import requests
content=requests.get("https://movie.douban.com/top250").text
soup=BeautifulSoup(content,"heml.parser")
all_prices=