from Utility import *
from Algorithms import *
import json

def main():
    util = Utility()
    util.robinhood_login()

    algo = Algorithms(util, "AAPL")





def pprint(s):
    print(json.dumps(s, indent=1))



if __name__ == "__main__":
    main()