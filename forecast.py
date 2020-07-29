import requests


def forecast(city):
    url = 'https://wttr.in/' + city + '?format=j1'

    try:
        response = requests.get(url).json()
        print(response)

        weather_now_json = response['current_condition'][0]
        print(weather_now_json)

        weather_now = city + ' - прогноз погоды: \n' \
                             '{0} \n' \
                             'Температура {1}..{2} °C \n' \
                             'Ветер {3} {4} m/s \n' \
                             'Давление {5} mmhg \n' \
                             'Влажность {6} % \n' \
                             'Видимость {7} km'.format(weather_now_json['weatherDesc'][0]['value'],
                                                       min(weather_now_json['FeelsLikeC'], weather_now_json['temp_C']),
                                                       max(weather_now_json['FeelsLikeC'], weather_now_json['temp_C']),
                                                       weather_now_json['winddir16Point'],
                                                       weather_now_json['windspeedKmph'],
                                                       weather_now_json['pressure'],
                                                       weather_now_json['humidity'],
                                                       weather_now_json['visibility'])

    except Exception:
        weather_now = 'Sorry, something goes wrong'

    return weather_now


if __name__ == '__main__':
    print(forecast('Kiyv'))