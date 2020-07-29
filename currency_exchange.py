import requests


def vals():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    res = ''

    try:
        response = requests.get(url).json()
        for el in response:
            if el['ccy'] == 'USD' or el['ccy'] == 'EUR':
                res += el['ccy']
                res += ' : '
                res += el['buy']
                res += '  '
                res += el['sale']
                res += '\n'

    except Exception:
        res = 'Sorry, something goes wrong'

    return res


if __name__ == '__main__':
    print(vals())
