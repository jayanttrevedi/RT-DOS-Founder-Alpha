"""
RT-DOS Intelligence Platform
Module      : Executive Workspace
Version     : 3.1.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st

from ui.market_health import show_market_health
from ui.market_breadth import MarketBreadthWidget
from ui.ranking import RankingPanel
from ui.summary import SummaryPanel


class Dashboard:

    def show(self, presentation):

        # ======================================================
        # Header
        # ======================================================

        st.title("📈 RT-DOS Intelligence Platform")

        left_header, right_header = st.columns([4, 1])

        with left_header:
            st.caption("Retail Trading Decision Operating System")

        with right_header:
            if presentation.get("generated_at"):
                st.caption(f"Updated : {presentation['generated_at']}")

        st.divider()

        # ======================================================
        # Executive KPI Cards
        # ======================================================

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "Assets",
            presentation["total_assets"],
        )

        col2.metric(
            "Watch",
            presentation["watch"],
        )

        col3.metric(
            "Buy",
            presentation["buy"],
        )

        col4.metric(
            "Strong Buy",
            presentation["strong_buy"],
        )

        col5.metric(
            "Avoid",
            presentation["avoid"],
        )

        st.divider()

        # ======================================================
        # Executive Workspace
        # ======================================================

        left, right = st.columns([1, 2])

        with left:

            st.subheader("🟢 Market Pulse")

            show_market_health(presentation["market_health"])

            st.metric(
                "Market Status",
                presentation["market_status"],
            )

        with right:

            SummaryPanel().show(presentation)

        st.divider()

        # ======================================================
        # Market Breadth
        # ======================================================

        MarketBreadthWidget().show(presentation)

        st.divider()

        # ======================================================
        # Top Opportunities
        # ======================================================

        st.subheader("🏆 Top Opportunities")

        cards = st.columns(5)

        top = presentation.get(
            "top_five",
            [],
        )

        for i, column in enumerate(cards):

            with column:

                if i < len(top):

                    item = top[i]

                    st.metric(
                        label=item["symbol"],
                        value=item["decision"],
                        delta=f"Score : {item['score']}",
                    )

        st.divider()

        # ======================================================
        # Complete Ranking
        # ======================================================

        with st.expander(
            "📋 Complete Market Intelligence Ranking",
            expanded=False,
        ):

            RankingPanel().show(presentation["ranked"])

        st.divider()

        # ======================================================
        # Footer
        # ======================================================

        st.caption("RT-DOS Platform v3.1 | Workspace Framework")
