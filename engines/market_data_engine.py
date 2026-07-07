"""
RT-DOS Founder Alpha
Market Data Engine
Version : 0.4.0
"""

from pathlib import Path
from engines.data_provider import DataProvider


class MarketDataEngine:

    def __init__(self):
        self.engine_name = "Market Data Engine"

    def load(self):

        watchlist_file = Path("data/watchlist.txt")
        watchlist = []

        if watchlist_file.exists():
            with open(watchlist_file, "r") as file:
                watchlist = [line.strip() for line in file if line.strip()]

        print("\nLoading Watchlist...\n")

        print(
            f"{'SYMBOL':12}"
            f"{'LTP':12}"
            f"{'OPEN':12}"
            f"{'HIGH':12}"
            f"{'LOW':12}"
            f"{'CLOSE':12}"
            f"{'VOLUME':12}"
        )

        print("-" * 84)

        provider = DataProvider()
        market_data = []

        for symbol in watchlist:

            data = provider.get_market_data(symbol)
            market_data.append(data)

            print(
                f"{data['symbol']:12}"
                f"{data['last_price']:12.2f}"
                f"{data['open']:12.2f}"
                f"{data['high']:12.2f}"
                f"{data['low']:12.2f}"
                f"{data['close']:12.2f}"
                f"{data['volume']:12}"
            )

        print(f"\n{len(watchlist)} symbols loaded.\n")

        return {
            "status": True,
            "engine": self.engine_name,
            "message": "Watchlist Loaded Successfully",
            "watchlist": watchlist,
            "market_data": market_data,
        }
