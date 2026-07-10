"""
RT-DOS Intelligence Platform
Module      : Executive Workspace
Version     : 3.2.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st

from ui.market_health import show_market_health
from ui.market_breadth import MarketBreadthWidget
from ui.opportunity_radar import OpportunityRadar
from ui.ranking import RankingPanel
from ui.summary import SummaryPanel


class Dashboard:

    def show(self, presentation):

        # ======================================================
        # Header
        # ======================================================

        st.title("📈 RT-DOS Intelligence Platform")

        header_left, header_right = st.columns([4, 1])

        with header_left:
            st.caption("Retail Trading Decision Operating System")

        with header_right:
            if presentation.get("generated_at"):
                st.caption(f"Updated : {presentation['generated_at']}")

        st.divider()

        # ======================================================
        # Executive KPI Cards
        # ======================================================

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Assets", presentation["total_assets"])
        col2.metric("Watch", presentation["watch"])
        col3.metric("Buy", presentation["buy"])
        col4.metric("Strong Buy", presentation["strong_buy"])
        col5.metric("Avoid", presentation["avoid"])

        st.divider()

        # ======================================================
        # Workspace
        # ======================================================

        left, right = st.columns([1, 2])

        with left:

            st.subheader("🟢 Market Pulse")

            show_market_health(presentation["market_health"])

            st.metric(
                "Market Status",
                presentation["market_status"],
            )

            st.divider()

            MarketBreadthWidget().show(presentation)

        with right:

            SummaryPanel().show(presentation)

            st.divider()

            OpportunityRadar().show(presentation)

        st.divider()

        # ======================================================
        # Top Opportunities
        # ======================================================

        st.subheader("🏆 Top Opportunities")

        cards = st.columns(5)

        top = presentation.get("top_five", [])

        for i, card in enumerate(cards):

            with card:

                if i < len(top):

                    item = top[i]

                    st.metric(
                        item["symbol"],
                        item["decision"],
                        f"Score : {item['score']}",
                    )

        st.divider()

        # ======================================================
        # Ranking
        # ======================================================

        with st.expander(
            "📋 Complete Market Intelligence Ranking",
            expanded=False,
        ):

            RankingPanel().show(presentation["ranked"])

        st.divider()

        st.caption("RT-DOS Platform v3.2 | Executive Workspace")
