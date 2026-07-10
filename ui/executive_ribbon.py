"""
RT-DOS Intelligence Platform
Module      : Executive Decision Ribbon
Version     : 1.0.0
Status      : Production
Architecture: Market Command Centre V2
"""

import streamlit as st


class ExecutiveRibbon:

    def show(self, presentation):

        top = presentation.get("top_opportunity")

        if top is None:
            return

        market_health = presentation["market_health"]
        market_status = presentation["market_status"]

        buying_pressure = self._buying_pressure(presentation)

        trend = self._trend(market_health)

        action = self._action(top["decision"])

        c1, c2, c3, c4, c5, c6 = st.columns(6)

        with c1:
            st.metric("Market Health", f"{market_health}%")

        with c2:
            st.metric("Buying Pressure", buying_pressure)

        with c3:
            st.metric("Trend", trend)

        with c4:
            st.metric("Risk", top["risk"])

        with c5:
            st.metric("Best Asset", top["symbol"])

        with c6:
            st.metric("Action", top["decision"])

        st.success(f"""
### ⭐ RT-DOS Executive Decision

**Market Status :** {market_status}

**Recommended Action :** {action}

**Highest Ranked Asset :** {top['symbol']}

**Confidence :** {top['confidence']}%
""")

        st.divider()

    # -----------------------------------------------------

    def _buying_pressure(self, presentation):

        buys = presentation["strong_buy"] + presentation["buy"]

        if buys >= 15:
            return "HIGH"

        if buys >= 8:
            return "MODERATE"

        return "LOW"

    # -----------------------------------------------------

    def _trend(self, health):

        if health >= 80:
            return "BULLISH"

        if health >= 60:
            return "POSITIVE"

        if health >= 40:
            return "NEUTRAL"

        return "BEARISH"

    # -----------------------------------------------------

    def _action(self, decision):

        mapping = {
            "STRONG BUY": "BUY QUALITY STOCKS",
            "BUY": "LOOK FOR LONG TRADES",
            "WATCH": "WAIT FOR CONFIRMATION",
            "HOLD": "REDUCE NEW POSITIONS",
            "AVOID": "CAPITAL PRESERVATION",
        }

        return mapping.get(decision, "WAIT")
