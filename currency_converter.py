import requests
import json
import pprint

class Converter:

  def __init__(self, code_currency: str, amount_of_money: float):
    self.code_currency = code_currency
    self.amount_of_money = amount_of_money

  def website_content(self):
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
    response = requests.get(url)
    page_content = response.json()

    return page_content

  def currency_converter(self):
    self.code_currency = self.code_currency.upper()
    data = self.website_content()[0]['rates']

    for i in range(len(data)):
      if data[i]['code'] == self.code_currency:
        polish_money = round(data[i]['mid'] * self.amount_of_money, 2)
        sentence = f'Twoje {self.amount_of_money} {self.code_currency} jest warte {polish_money} PLN'

        return sentence

  def actual_exchange_rate(self):
    self.code_currency = self.code_currency.upper()
    data = self.website_content()[0]
    date = data['effectiveDate']
    data_exchange_rate = data['rates']

    for i in range(len(data_exchange_rate)):
      if data_exchange_rate[i]['code'] == self.code_currency:
        
        exchange_rate = data_exchange_rate[i]['mid']
        sentence = f'Kurs wymiany z dnia {date} wynosi {exchange_rate}'

        return sentence

euro_pln = Converter('eur', 2011)
pprint.pprint(euro_pln.currency_converter())
pprint.pprint(euro_pln.actual_exchange_rate())
