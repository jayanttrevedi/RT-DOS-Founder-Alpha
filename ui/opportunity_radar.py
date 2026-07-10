"""
RT-DOS Intelligence Platform
Module      : Opportunity Radar
Version     : 3.0.0
Status      : Production
Architecture: Market Command Centre V3
"""

import streamlit as st


class OpportunityRadar:

    # ==========================================================
    # Public
    # ==========================================================

    def show(self, presentation):

        opportunities = presentation.get("top_five", [])

        st.subheader("🎯 RT-DOS Opportunity Radar")

        if not opportunities:

            st.info("No opportunities available.")

            return

        for asset in opportunities:

            self._show_card(asset)

    # ==========================================================
    # Private
    # ==========================================================

    def _show_card(self, asset):

        symbol = asset.get("symbol", "-")
        decision = asset.get("decision", "-")
        score = asset.get("score", 0)

        confidence = asset.get(
            "institutional_confidence",
            asset.get("confidence", 0),
        )

        probability = asset.get(
            "probability",
            0,
        )

        expected_move = asset.get(
            "expected_move",
            "-",
        )

        holding = asset.get(
            "holding_period",
            "-",
        )

        risk_reward = asset.get(
            "risk_reward",
            "-",
        )

        regime = asset.get(
            "market_regime",
            "-",
        )

        grade = asset.get(
            "confidence_grade",
            "-",
        )

        with st.container(border=True):

            left, right = st.columns([3, 1])

            with left:

                st.markdown(f"## {symbol}")

                st.markdown(f"**Decision:** {decision}")

                st.markdown(f"**Market Regime:** {regime}")

            with right:

                st.metric(
                    "Score",
                    score,
                )

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "ICI",
                    confidence,
                )

            with c2:

                st.metric(
                    "Probability",
                    f"{probability}%",
                )

            with c3:

                st.metric(
                    "Grade",
                    grade,
                )

            c4, c5 = st.columns(2)

            with c4:

                st.metric(
                    "Expected Move",
                    expected_move,
                )

            with c5:

                st.metric(
                    "Holding",
                    holding,
                )

            st.metric(
                "Risk / Reward",
                risk_reward,
            )

            st.divider()
