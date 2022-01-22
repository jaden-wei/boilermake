from this import d
import robin_stocks.robinhood as r

from urllib.request import urlopen
import json

from secret import *

def get_json_from_url(url):
    response = urlopen(url)
    data_json = json.loads(response.read())
    print(data_json)

def pprint(s):
    print(json.dumps(s, index=1))

class Utility:

    def robinhood_login(self):
        r.login(username=USERNAME, password=PASSWORD, expiresIn=86400, by_sms=True)
        print("Logged into Robinhood")

    def robinhood_logout(self):
        r.logout()
        print("Logged out of Robinhood")

    def get_info(self, symbol):
        print(r.stocks.get_stock_quote_by_symbol(symbol))

    def get_price_history(self, symbol):
        pprint(r.stocks.get_stock_historicals(symbol))

    def place__market_order(self, symbol, quantity):
        pprint(r.orders.order_buy_market(symbol=symbol, quantity=quantity))
    
    def place_limit_order(self, symbol, quantity, price):
        pprint(r.orders.order_buy_limit(symbol, quantity, price))


u = Utility()

u.robinhood_login()

u.get_price_history("AAPL")

