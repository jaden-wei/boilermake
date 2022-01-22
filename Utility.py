import robin_stocks.robinhood as r

from urllib.request import urlopen
import json

class Utility:
    def __init__(self):
        print("Initialized")

    def robinhood_login(user, pw):
        r.login(username=user, password=pw, expiresIn=86400, by_sms=True)
        print("Logged into Robinhood")

    def robinhood_logout():
        r.logout()
        print("Logged out of Robinhood")

    def getInfo(ticker):
        print(r.stocks.get_stock_quote_by_symbol(ticker))

url = r.stocks.get_100_most_popular_url()
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)