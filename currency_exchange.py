import requests
import sys


def vals():

    myUrl = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    res = ''

    try:
        response = requests.get(myUrl).json()
        for el in response:
            if el['ccy'] == 'USD' or el['ccy'] == 'EUR':
                res += el['ccy']
                res += ' : '
                res += el['buy']
                res += '  '
                res += el['sale']
                res += '\n'

    except Exception:
       print(sys.exc_info()[1])

    return res


if __name__ == '__main__':
    print(vals())
