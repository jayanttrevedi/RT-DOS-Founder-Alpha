"""
RT-DOS Founder Alpha
Data Provider
Version : 0.5.0
"""

import yfinance as yf


class DataProvider:

    INDEX_SYMBOLS = {
        "NIFTY": "^NSEI",
        "BANKNIFTY": "^NSEBANK",
        "FINNIFTY": "NIFTY_FIN_SERVICE.NS",
        "MIDCPNIFTY": "^NSEMDCP50",
    }

    def get_market_data(self, symbol):

        # -----------------------------
        # Resolve Yahoo Finance Symbol
        # -----------------------------

        if symbol in self.INDEX_SYMBOLS:

            ticker_symbol = self.INDEX_SYMBOLS[symbol]

        else:

            # Automatically map NSE stocks
            ticker_symbol = f"{symbol}.NS"

        try:

            ticker = yf.Ticker(ticker_symbol)

            history = ticker.history(
                period="60d",
                interval="1d",
                auto_adjust=False,
            )

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
                "history": history,
            }

        except Exception as e:

            print(f"[DataProvider] {symbol} ({ticker_symbol}) : {e}")

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
