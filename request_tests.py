import requests
from bs4 import BeautifulSoup


def make_request(url):
    res = requests.get(url)
    print(f'for request to: {url}; status: {res.status_code}')
    soup = BeautifulSoup(res.content)
    print(soup.find('h2', {'id': 'answer'}).prettify())
    print()
    print()


make_request('https://next-day.herokuapp.com/?day=1&month=2&year=2000')

make_request('https://next-day.herokuapp.com/?day=a&month=b&year=c')
