import ccxt
import time
import random
import sqlite3

"""
    CryptoFetch is a crude app maintained by NYU-ML Club.
    This app fetches price data from crypto exchanges specified by show_exchanges() method.
    Any inquiries about this program, please email: ph1335@nyu.edu
    
    This program is written with CCXT API. Huge kudus to these guys! Wonderful job!
"""

class CryptoFetchtron:
    """
        In your init specify which exchange you'd like to connect to. 
        This is slow connection in order not to get ban.
        By default, we're fetching from Binance.com.
    """
    def __init__(self, exchange_name="binance"):
        exchange_class = getattr(ccxt, exchange_name)
        self.exchange = exchange_class({
            'enableRateLimit': True,
        })
    
    def connect_to_db(self, path):
        """
            This specifies where file with db should be stored
            :@param: path is string with absolute path to the directory where data
                     from exchange should be stored

            TODO: we should make default behavior to create dir in the current working directory
        """
        conn = sqlite3.connect(path + "crypto.sqlite")
        self.db = conn.cursor()

    #  this queries orderbook 
    def get_current_orderbook(self, pair="BTC/USDT", limit=5, delay=10):
        """
            :@param limit: integer - how many order book elements are fetched at once.
            :@param delay: integer - how many seconds to wait before next fetch of order book is made

            This method fetches current market values for ask/bid orders and prices. Time is current @ your location.
        """
        if self.exchange.has['fetchOrders']:
            while True:
                orderbook = self.exchange.fetch_order_book(pair, limit)
                print orderbook
                # bids = orderbook['bids']
                # asks = orderbook['asks']
                # current_time = time.asctime(time.localtime(time.time()))
                # for i in range(len(bids)):
                #     print("Pair: {}. Timestamp:{}.\nOrder price: ${} @ Quantity of {} and Asks price: ${} @ Quantity of {}.\n"
                #             .format(pair, current_time, bids[i][0], bids[i][1], asks[i][0], asks[i][1]))
                time.sleep(delay)

    #  this should be used for static pooling the exchange (real-time data fetch)
    def get_current_price_data(self, ticker="BTC/USDT", delay=10):
        if(self.exchange.has['fetchTicker']):
            print("############## THE FETCH STREAM BEGINS NOW ################### (to interupt C-c)")
            while True:
                data = self.exchange.fetch_ticker(ticker)['info']
                # print(data)
                print("symbol: {}, last price: {}, last qty: {}"\
                        .format(data["symbol"], data["lastPrice"], data["lastQty"]))
                print("askPrice: {}, askQty: {}, bidPrice: {}, bidQty: {}"\
                    .format(data["askPrice"], data["askQty"], data["bidPrice"], data["bidQty"]))
                time.sleep(delay)

    def get_timeframes(self):
        try:
            print("Timeframes for {} are {}".format(self.exchange.name, self.exchange.timeframe))
        except:
            print("{} doesn't have specified timeframes".format(self.exchange.name))
            return

    def show_pairs(self, pair_group="BTC"):
        """
            :@param pair_group: String - btc, eth, bnb, usdt... must be in capital
            
            This method only shows possible pairs with the pair_group. 
            For example, BLZ/ETH pair for ETH group.
        """
        tickers = list(self.exchange.markets.keys())
        for i in tickers:
            if i[-3:] == pair_group:
                print(i)

def show_exchanges():
    markets = list(ccxt.exchanges)
    print("################MARKETS#################")
    for i in markets:
        print(i)
    print("################THE END#################")

if __name__ == '__main__':
    #  for full list of exchanges, please visit this link: https://github.com/ccxt/ccxt/wiki/Manual#instantiation
    # show_exchanges()
    exchange = CryptoFetchtron()

    #  this function takes absolute path where the file.db will be stored
    exchange.connect_to_db("/home/peterson/Desktop/FinApp/NYU-ML/CryptoFetchtron/crypto_data/")

    # exchange.get_timeframes()
    # exchange.show_pairs('BTC')
    # exchange.get_data_current()
    exchange.get_current_price_data("BTC/USDT")