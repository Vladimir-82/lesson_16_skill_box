from bs4 import BeautifulSoup
import requests

response = requests.get('https://meduza.io/')
# print(response.text)
sours = "ExchangeRates-item"

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_values = html_doc.find_all('div', 'ExchangeRates-root' if )
    # list_of_names = html_doc.find_all('td', {'class': 'home-link ho<div class)

    # for names, values in zip(list_of_names, list_of_values):
    #     print(names.text, values.text)
    print(list_of_values)