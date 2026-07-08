"""
RT-DOS Intelligence Platform
Dashboard
Version : 2.0.0
"""

import streamlit as st

from ui.market_health import show_market_health
from ui.ranking import RankingPanel
from ui.summary import SummaryPanel


class Dashboard:

    def show(self, presentation):

        st.title("📈 RT-DOS Intelligence Platform")

        st.subheader("Founder Alpha Prototype")

        st.caption("Intelligence Before Execution")

        st.divider()

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Assets", presentation["total_assets"])

        col2.metric("Watch", presentation["watch"])

        col3.metric("Buy", presentation["buy"])

        col4.metric("Strong Buy", presentation["strong_buy"])

        col5.metric("Avoid", presentation["avoid"])

        st.divider()

        left, right = st.columns([1, 2])

        with left:

            show_market_health(presentation["market_health"])

        with right:

            SummaryPanel().show(presentation)

        st.divider()

        RankingPanel().show(presentation["ranked"])

        st.divider()

        st.caption("RT-DOS Founder Alpha | Version 2.0")
