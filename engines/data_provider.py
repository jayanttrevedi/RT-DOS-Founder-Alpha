"""
RT-DOS Intelligence Platform
Module      : Data Provider
Version     : 1.0.1
Status      : Production
Architecture: Core Intelligence Layer
"""

import math

import yfinance as yf


class DataProvider:

    INDEX_SYMBOLS = {
        "NIFTY": "^NSEI",
        "BANKNIFTY": "^NSEBANK",
        "FINNIFTY": "NIFTY_FIN_SERVICE.NS",
        "MIDCPNIFTY": "^NSEMDCP50",
    }

    ALTERNATE_SYMBOLS = {
        "NIFTY": [
            "^NSEI",
        ],
        "BANKNIFTY": [
            "^NSEBANK",
        ],
        "FINNIFTY": [
            "NIFTY_FIN_SERVICE.NS",
            "^CNXFINSERVICE",
        ],
        "MIDCPNIFTY": [
            "^NSEMDCP50",
        ],
    }

    def get_market_data(self, symbol):

        ticker_symbol = self.INDEX_SYMBOLS.get(
            symbol,
            f"{symbol}.NS",
        )

        try:

            ticker = yf.Ticker(ticker_symbol)

            history = ticker.history(
                period="60d",
                interval="1d",
                auto_adjust=False,
            )

            if history.empty:
                raise ValueError("No market data returned")

            history = history.dropna(subset=["Close"])

            if history.empty:
                raise ValueError("No valid closing prices found")

            latest = history.iloc[-1]

            close = float(latest["Close"])

            if math.isnan(close):
                raise ValueError("Latest close price is NaN")

            open_price = float(latest["Open"])
            high = float(latest["High"])
            low = float(latest["Low"])

            volume = latest["Volume"]

            if volume != volume:
                volume = 0

            volume = int(volume)

            return {
                "symbol": symbol,
                "last_price": close,
                "open": open_price,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "history": history,
            }

        except Exception as e:

            print("=" * 80)
            print("DATA PROVIDER ERROR")
            print(f"Symbol       : {symbol}")
            print(f"Yahoo Symbol : {ticker_symbol}")
            print(f"Reason       : {e}")
            print("=" * 80)

            return {
                "symbol": symbol,
                "last_price": 0.0,
                "open": 0.0,
                "high": 0.0,
                "low": 0.0,
                "close": 0.0,
                "volume": 0,
                "history": None,
            }
