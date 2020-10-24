import requests
import re

while True:
    main_input = input("Wprowadź kwotę i skrót waluty bazowej: ").replace(" ", "")
    try:
        base_currency = re.findall(r'\D+', main_input)[0].upper()
        break
    except IndexError:
        print("Wprowadź przynajmniej skrót waluty")

try:
    amount = float(re.findall(r'\d+', main_input)[0])
except IndexError:
    amount = 1

target_currency = input("Wprowadź skrót waluty docelowej: ").upper().replace(" ", "")

parameters = {
    "base": base_currency
}

exchange_rate_p = requests.get("https://api.exchangeratesapi.io/latest", params=parameters)

try:
    for key, val in exchange_rate_p.json()["rates"].items():
        if key == target_currency:
            print("{} {} - {} {}".format(amount, base_currency, round(amount * val, 2), key))
except KeyError:
    print("invalid input")
