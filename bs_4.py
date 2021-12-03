from bs4 import BeautifulSoup
import requests

response = requests.get('http://belta.by/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    citys = html_doc.find_all('span', {'id': "cityNameIn_header"})
    temp = html_doc.find_all('a', {'href': '/meteo/'})

    for city, t in zip(citys, temp):
        print(city.text, t.text.strip())

    # city = html_doc.find('span', {'id': "cityNameIn_header"})
    # print(city.text.strip())
    #
    # temp = html_doc.find('a', {'href': '/meteo/'})
    # print(temp.text.strip())



# if response.status_code == 200:
#     html_doc = BeautifulSoup(response.text, features='html.parser')
#     list_of_values = html_doc.find_all('span', {'class': 'inline-stocks__value_inner'})
#     list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})
#
#     for names, values in zip(list_of_names, list_of_values):
#         print(names.text, values.text)
