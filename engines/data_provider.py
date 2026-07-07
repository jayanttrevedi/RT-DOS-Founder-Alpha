"""
RT-DOS Founder Alpha
Data Provider
Version : 0.1.0
"""


class DataProvider:

    def get_market_data(self, symbol):

        sample_data = {
            "symbol": symbol,
            "last_price": 100.00,
            "open": 99.50,
            "high": 101.20,
            "low": 98.80,
            "close": 99.90,
            "volume": 1250000,
        }

        return sample_data
