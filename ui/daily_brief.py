"""
RT-DOS Intelligence Platform
Module      : Daily Executive Brief
Version     : 4.0.0
Status      : Production Ready
Architecture: RT-DOS Presentation Engine V4
"""

import streamlit as st


class DailyBrief:
    """Presentation-only daily executive brief component."""

    def show(self, presentation):
        """Render the daily executive brief from presentation data only."""

        if not isinstance(presentation, dict):
            st.error("Presentation data is unavailable.")
            return

        executive = presentation.get("executive") or {}

        if not isinstance(executive, dict):
            executive = {}

        st.title("Daily Executive Brief")
        st.caption("RT-DOS Presentation Engine V4")

        metric_columns = st.columns(4)

        with metric_columns[0]:
            st.metric("Market Health", presentation.get("market_health", "N/A"))

        with metric_columns[1]:
            st.metric("Market Status", presentation.get("market_status", "N/A"))

        with metric_columns[2]:
            st.metric("Total Assets", presentation.get("total_assets", "N/A"))

        with metric_columns[3]:
            top_opportunity = presentation.get("top_opportunity") or {}
            recommendation = "N/A"

            if isinstance(top_opportunity, dict):
                symbol = top_opportunity.get("symbol", "N/A")
                decision = top_opportunity.get("decision", "N/A")

                if symbol != "N/A" and decision != "N/A":
                    recommendation = f"{symbol} - {decision}"
                elif symbol != "N/A":
                    recommendation = symbol
                elif decision != "N/A":
                    recommendation = decision

            st.metric("Top Recommendation", recommendation)

        st.divider()

        st.subheader("Executive Summary")

        summary_columns = st.columns(2)

        with summary_columns[0]:
            st.write(f"Market Bias: {executive.get('market_bias', 'N/A')}")
            st.write(f"Market Regime: {executive.get('market_regime', 'N/A')}")
            st.write(
                f"Institutional Confidence: {executive.get('institutional_confidence', 'N/A')}"
            )

        with summary_columns[1]:
            st.write(f"Probability: {executive.get('probability', 'N/A')}")
            st.write(f"Expected Move: {executive.get('expected_move', 'N/A')}")
            st.write(f"Holding Period: {executive.get('holding_period', 'N/A')}")

        st.divider()

        st.subheader("Trading Plan")
        st.info(executive.get("trading_plan", "N/A"))

        st.divider()

        st.subheader("Executive Commentary")
        st.success(executive.get("executive_comment", "N/A"))

        st.divider()

        st.subheader("Risk Watch")
        risk_watch = executive.get("risk_watch") or []

        if isinstance(risk_watch, list) and risk_watch:
            for item in risk_watch:
                st.markdown(f"- {item}")
        else:
            st.write("No risk watch items available.")
