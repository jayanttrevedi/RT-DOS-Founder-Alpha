"""
RT-DOS Intelligence Platform
Module      : Executive Workspace
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

import streamlit as st

from ui.market_health import show_market_health
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

            if presentation["generated_at"]:

                st.caption(f"Updated : {presentation['generated_at']}")

        st.divider()

        # ======================================================
        # Executive KPI Cards
        # ======================================================

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Assets",
                presentation["total_assets"],
            )

        with col2:
            st.metric(
                "Watch",
                presentation["watch"],
            )

        with col3:
            st.metric(
                "Buy",
                presentation["buy"],
            )

        with col4:
            st.metric(
                "Strong Buy",
                presentation["strong_buy"],
            )

        with col5:
            st.metric(
                "Avoid",
                presentation["avoid"],
            )

        st.divider()

        # ======================================================
        # Executive Workspace
        # ======================================================

        left, right = st.columns([1, 2])

        # ------------------------
        # Left
        # ------------------------

        with left:

            st.subheader("🟢 Market Pulse")

            show_market_health(presentation["market_health"])

            st.metric(
                "Market Status",
                presentation["market_status"],
            )

        # ------------------------
        # Right
        # ------------------------

        with right:

            st.subheader("🧠 Executive Intelligence")

            SummaryPanel().show(presentation)

        st.divider()

        # ======================================================
        # Top Opportunities
        # ======================================================

        st.subheader("🏆 Top Opportunities")

        cards = st.columns(5)

        top = presentation.get("top_five", [])

        for i in range(5):

            with cards[i]:

                if i < len(top):

                    item = top[i]

                    st.metric(
                        label=item["symbol"],
                        value=item["decision"],
                        delta=f"Score : {item['score']}",
                    )

                else:

                    st.empty()

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

        # ======================================================
        # Footer
        # ======================================================

        st.caption("RT-DOS Platform v3.0 | Workspace Architecture")
