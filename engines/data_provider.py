"""
RT-DOS Founder Alpha
Data Provider
Version : 0.2.1
"""

import yfinance as yf


class DataProvider:

    SYMBOL_MAP = {
        "NIFTY": "^NSEI",
        "BANKNIFTY": "^NSEBANK",
        "FINNIFTY": "NIFTY_FIN_SERVICE.NS",
        "MIDCPNIFTY": "^NSEMDCP50",
        "RELIANCE": "RELIANCE.NS",
    }

    def get_market_data(self, symbol):

        ticker_symbol = self.SYMBOL_MAP.get(symbol, symbol)

        try:
            ticker = yf.Ticker(ticker_symbol)

            history = ticker.history(period="5d")

            if history.empty:
                raise ValueError("No market data returned")

            latest = history.iloc[-1]

            return {
                "symbol": symbol,
                "last_price": float(latest["Close"]),
                "open": float(latest["Open"]),
                "high": float(latest["High"]),
                "low": float(latest["Low"]),
                "close": float(latest["Close"]),
                "volume": int(latest["Volume"]),
            }

        except Exception:

            return {
                "symbol": symbol,
                "last_price": 0.0,
                "open": 0.0,
                "high": 0.0,
                "low": 0.0,
                "close": 0.0,
                "volume": 0,
            }
