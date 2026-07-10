"""
RT-DOS Intelligence Platform
Module      : Market Command Centre Header
Version     : 1.0.0
Status      : Production
Architecture: Workspace Framework
"""

from datetime import datetime, time

import streamlit as st


class MarketHeader:

    VERSION = "Founder Alpha v3.2"

    # ---------------------------------------------------------

    def show(self):

        left, centre, right = st.columns([4, 2, 2])

        with left:

            st.title("📈 RT-DOS Market Command Centre")

            st.caption("Retail Trading Decision Operating System")

        with centre:

            session = self._market_session()

            indicator = {
                "PRE-OPEN": "🟡",
                "OPEN": "🟢",
                "CLOSED": "🔴",
            }[session]

            st.metric(
                "Market Session",
                f"{indicator} {session}",
            )

        with right:

            now = datetime.now()

            st.metric(
                "Last Update",
                now.strftime("%d-%b-%Y\n%H:%M:%S"),
            )

        st.caption(
            f"RT-DOS {self.VERSION}  |  Data Source : Yahoo Finance  |  Workspace : Market Command Centre"
        )

        st.divider()

    # ---------------------------------------------------------

    def _market_session(self):

        now = datetime.now().time()

        pre_open_start = time(9, 0)
        market_open = time(9, 15)
        market_close = time(15, 30)

        if pre_open_start <= now < market_open:
            return "PRE-OPEN"

        if market_open <= now <= market_close:
            return "OPEN"

        return "CLOSED"
