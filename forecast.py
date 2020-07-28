import requests
import sys


def forecast(city):
    myUrl = 'https://wttr.in/' + city + '?0mM'

    try:
        response = requests.get(myUrl)
        return str(response.content, encoding='utf-8')

    except Exception:
        print(sys.exc_info()[1])
        return ''


def testing():
    url = 'https://wttr.in/Kyiv?0mM'

    response = requests.get(url)
    print(str(response.content, encoding='utf-8'))


if __name__ == '__main__':
    testing()
