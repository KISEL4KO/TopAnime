import requests
from bs4 import BeautifulSoup

# init func
def init():
   #create url and made request
    url = 'https://yummyanime.tv/2top-100/'
    page = requests.get(url)

    #made soup for reading html
    soup = BeautifulSoup(page.text, "html.parser")

    #create 2 lists
    filteredAnime = []
    allAnime= []

    #reading only div with class movie-item__title in html
    allAnime = soup.findAll('div',class_='movie-item__title')

    #sort and add only anime in filteredAnime list
    for data in allAnime:
            filteredAnime.append(data.text)

    #eding list that will be only 5 names
    filteredAnime = filteredAnime[:5]

    return filteredAnime

