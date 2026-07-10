"""
RT-DOS Intelligence Platform
Module      : Market Command Centre
Version     : 5.0.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st

from engines.market_sentinel_engine import MarketSentinelEngine
from engines.position_guardian_engine import PositionGuardianEngine
from ui.market_header import MarketHeader
from ui.daily_brief import DailyBrief
from ui.executive_alerts import ExecutiveAlerts
from ui.executive_ribbon import ExecutiveRibbon
from ui.market_health import show_market_health
from ui.market_breadth import MarketBreadthWidget
from ui.opportunity_radar import OpportunityRadar
from ui.position_guardian import PositionGuardian
from ui.summary import SummaryPanel
from ui.ranking import RankingPanel


class Dashboard:

    def show(self, presentation):

        # =====================================================
        # Header
        # =====================================================

        MarketHeader().show()

        sentinel = MarketSentinelEngine().analyze()

        guardian = PositionGuardianEngine().analyze(
            presentation,
            sentinel,
        )

        DailyBrief().show(presentation)

        ExecutiveAlerts().show(sentinel)

        PositionGuardian().show(guardian)

        # =====================================================
        # Executive Decision Ribbon
        # =====================================================

        ExecutiveRibbon().show(presentation)

        # =====================================================
        # Executive KPI Strip
        # =====================================================

        k1, k2, k3, k4, k5 = st.columns(5)

        with k1:
            st.metric(
                "Assets",
                presentation["total_assets"],
            )

        with k2:
            st.metric(
                "Strong Buy",
                presentation["strong_buy"],
            )

        with k3:
            st.metric(
                "Buy",
                presentation["buy"],
            )

        with k4:
            st.metric(
                "Watch",
                presentation["watch"],
            )

        with k5:
            st.metric(
                "Avoid",
                presentation["avoid"],
            )

        st.divider()

        # =====================================================
        # Main Workspace
        # =====================================================

        left, right = st.columns([1, 2])

        with left:

            st.subheader("📡 Market Pulse")

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

        # =====================================================
        # Top Opportunities
        # =====================================================

        st.subheader("🏆 Top Opportunities")

        cards = st.columns(5)

        top = presentation.get(
            "top_five",
            [],
        )

        for index, card in enumerate(cards):

            with card:

                if index < len(top):

                    item = top[index]

                    st.metric(
                        item["symbol"],
                        item["decision"],
                        delta=f"Score {item['score']}",
                    )

        st.divider()

        # =====================================================
        # Ranking
        # =====================================================

        with st.expander(
            "📋 Complete Market Intelligence Ranking",
            expanded=False,
        ):

            RankingPanel().show(presentation["ranked"])

        st.divider()

        st.caption("RT-DOS Founder Alpha | Market Command Centre V2")
