from typing import Optional

import requests
from bs4 import BeautifulSoup


def get_animals_by_url(url: str) -> tuple[Optional[list], Optional[str]]:
    response = requests.get(
        url=url
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("div", {"class": "mw-category mw-category-columns"})
    if not table:
        return None, None
    animals = [animal.text for animal in table.find_all('li')]

    next_page = soup.find_all('a', {'title': 'Категория:Животные по алфавиту'})[-1]['href']
    next_page = 'https://ru.wikipedia.org' + next_page

    return animals, next_page


animals_dict = {}
animals, next_page = get_animals_by_url('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')

iteration = 0
stop = False
while True:
    for animal in animals:
        first_char = animal[0]
        if first_char == 'A':
            stop = True
            break
        if first_char not in animals_dict:
            animals_dict[first_char] = 0
        else:
            animals_dict[first_char] += 1

    if stop:
        break
    animals, next_page = get_animals_by_url(next_page)
    if not animals:
        break

    print(f"Iteration: {iteration}, dict status: {animals_dict}")
    iteration += 1


print(animals_dict)
