class Algorithms:
    def __init__(self, util, symbol):
        self.util = util
        self.symbol = symbol
        self.data = util.get_price_history(symbol)
        self.quantity = 0 # keep track of quantity of current symbol

    # calculate the average volatility of the stock in the past year
    # need open price of current day
    # calculate lower bound => buy
    # calculate upper bound => sell

    def mean_reversion(self):
        avg_var = self.get_avg_variance()
        open_price = self.data[len(self.data) - 1].open_price
        price = self.util.get_price()

        if (price < open_price - (avg_var / 2)):
            # calculate how much we want to buy
            dollars = 100 * (open_price - (avg_var / 2) - price)
            # place buy
            self.util.place_market_order(self.symbol, dollars)
            # add to quantity
            self.quantity += dollars / price

        elif (self.util.get_price() > open_price + (avg_var / 2)):
            self.util.place_sell_order(self.symbol, self.quantity)

    def get_avg_variance(self):
        var_sum = 0

        for pt in self.data:
            diff = pt.high_price - pt.low_price
            var_sum += diff
        
        return var_sum / len(self.data)


