"""
A module which scrapes the empire website and gets the list of 100 most viewed sites
then saves the movie title in the movies.txt file
"""
from bs4 import BeautifulSoup
import requests

# make soup from website contents
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, "html.parser")
# get list of movie titles
titles = soup.find_all(name='h3', class_='title')
title_list = [title.getText().split(')')[-1] for title in titles]

# reverse the list that is attained so as to list from 1-100 and not 100-1
title_list = title_list[::-1]

# write the titles in the movies.txt file
for title in title_list:
    with open('movies.txt', 'w') as file:
        pos = 1
        for title in title_list:
            file.write(f"{pos}) {title}\n")
            pos += 1