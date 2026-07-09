"""
RT-DOS Intelligence Platform
Module      : Market Breadth Widget
Version     : 1.0.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st


class MarketBreadthWidget:

    def show(self, presentation):

        total = presentation.get("total_assets", 0)

        if total == 0:
            st.info("No market breadth available.")
            return

        strong_buy = presentation.get("strong_buy", 0)
        buy = presentation.get("buy", 0)
        watch = presentation.get("watch", 0)
        hold = presentation.get("hold", 0)
        avoid = presentation.get("avoid", 0)

        def pct(value):
            return round((value / total) * 100, 1)

        st.subheader("📊 Market Breadth")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Strong Buy",
                f"{pct(strong_buy)}%",
                strong_buy,
            )

        with col2:
            st.metric(
                "Buy",
                f"{pct(buy)}%",
                buy,
            )

        with col3:
            st.metric(
                "Watch",
                f"{pct(watch)}%",
                watch,
            )

        with col4:
            st.metric(
                "Hold",
                f"{pct(hold)}%",
                hold,
            )

        with col5:
            st.metric(
                "Avoid",
                f"{pct(avoid)}%",
                avoid,
            )

        st.progress(presentation["market_health"] / 100)

        st.caption(f"Overall Market Health : {presentation['market_health']}%")
