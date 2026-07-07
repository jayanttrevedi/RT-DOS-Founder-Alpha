"""
RT-DOS Founder Alpha
Market Data Engine
Version : 0.3.0
"""

from pathlib import Path


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

        for symbol in watchlist:
            print(f"• {symbol}")

        print(f"\n{len(watchlist)} symbols loaded.\n")

        return {
            "status": True,
            "engine": self.engine_name,
            "message": "Watchlist Loaded Successfully",
            "watchlist": watchlist,
        }
