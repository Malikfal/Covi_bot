import requests

def cheapshark_api(game_name):
    req = requests.get("https://www.cheapshark.com/api/1.0/games?title=&storeID=1&limit=5")
    json = req.json()
    print(json)


def covid_api():
    req = requests.get("https://covid-api.com/api/reports/total?date=2023-03-09&iso=CHN")
    req2 = requests.get("https://covid-api.com/api/reports/total?date=2023-03-09&iso=RUS")

    json1 = req.json()['data']['active']
    json2 = req2.json()['data']['active']
    print(json1,json2)

    return f'На данный момент в России {json2} заболевших.\nПо сравнению с Китаем {json1}'
