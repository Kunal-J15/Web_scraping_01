import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


data = requests.get(URL).text
soup = BeautifulSoup(data, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles = titles[::-1]
titles = [a.text+"\n" for a in titles]
print(titles)
with open("Movies.txt","w") as file:
    for i in titles:
        file.write(i)