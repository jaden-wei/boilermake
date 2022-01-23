from this import d
import robin_stocks.robinhood as r

import json

from secret import *

class Utility:
    def __init__(self):
        self = self

    def robinhood_login(self):
        r.login(username=USERNAME, password=PASSWORD, expiresIn=86400, by_sms=True)
        print("Logged into Robinhood")

    def robinhood_logout(self):
        r.logout()
        print("Logged out of Robinhood")

    def get_info(self, symbol):
        print(r.stocks.get_stock_quote_by_symbol(symbol))

    def get_price(self, symbol):
        return(r.stocks.get_pricebook_by_symbol(symbol))

    def get_price_history(self, symbol):
        return r.stocks.get_stock_historicals(symbol, interval='day', span='year')

    def place_market_order(self, symbol, price):
        return r.orders.order_buy_fractional_by_price(symbol=symbol, amountInDollars=price)
    
    def place_limit_order(self, symbol, quantity, price):
        return r.orders.order_buy_limit(symbol, quantity, price)

    def place_sell_order(self, symbol, quantity):
        return r.orders.order_sell_fractional_by_quantity(symbol, quantity);

    def place_limit_sell_order(self, symbol, quantity, price):
        return r.orders.order_sell_limit(symbol, quantity, price)
