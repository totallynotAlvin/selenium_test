import requests
from bs4 import BeautifulSoup


def make_request(url, expected):
    res = requests.get(url)
    print(f'for request to: {url}; status: {res.status_code}')
    soup = BeautifulSoup(res.content, "html.parser")
    answer = soup.find('h2', {'id': 'answer'})
    print(answer.prettify())
    if expected in answer.text:
        print("passed")
    else:
        print("failed")
    print()


print("v1 tests")
make_request('https://next-day.herokuapp.com/?day=1&month=2&year=2000', "02 February 2000")

make_request('https://next-day.herokuapp.com/?day=a&month=b&year=c', "Something went wrong... Check your input")

make_request('https://next-day.herokuapp.com/?day=28&month=2&year=2022', "01 March 2022")

print("v2 tests")

make_request('https://next-day.herokuapp.com/v2/?day=1&month=2&year=2000', "02 February 2000")

make_request('https://next-day.herokuapp.com/v2/?day=a&month=b&year=c', "Something went wrong... Check your input")

make_request('https://next-day.herokuapp.com/v2/?day=28&month=2&year=2022', "01 March 2022")
