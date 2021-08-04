import requests
from pprint import pprint as print
# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/404d0b84fe6853334ff4a0ba/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()
data2 = response.json()['conversion_rate']

# Your JSON object
print(data)
print(data2)
