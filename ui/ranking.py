"""
RT-DOS Intelligence Platform
Module      : Professional Ranking Panel
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

import pandas as pd
import streamlit as st


class RankingPanel:

    def show(self, ranked):

        st.subheader("🏆 Market Intelligence Ranking")

        st.caption("Assets ranked by RT-DOS Composite Intelligence")

        if not ranked:

            st.info("No market intelligence available.")

            return

        table = (
            pd.DataFrame(ranked)
            .sort_values(
                by="score",
                ascending=False,
            )
            .reset_index(drop=True)
        )

        # -------------------------------------------------
        # Ranking
        # -------------------------------------------------

        medals = []

        for index in range(len(table)):

            if index == 0:

                medals.append("🥇")

            elif index == 1:

                medals.append("🥈")

            elif index == 2:

                medals.append("🥉")

            else:

                medals.append(str(index + 1))

        table.insert(0, "Rank", medals)

        # -------------------------------------------------
        # Formatting
        # -------------------------------------------------

        table["score"] = table["score"].astype(int).astype(str)

        table["confidence"] = table["confidence"].astype(int).astype(str) + "%"

        decision_map = {
            "STRONG BUY": "🟢 STRONG BUY",
            "BUY": "🟢 BUY",
            "WATCH": "🟡 WATCH",
            "HOLD": "🟠 HOLD",
            "AVOID": "🔴 AVOID",
        }

        risk_map = {
            "LOW": "🟢 LOW",
            "MEDIUM": "🟡 MEDIUM",
            "HIGH": "🔴 HIGH",
        }

        table["decision"] = table["decision"].map(decision_map)

        table["risk"] = table["risk"].map(risk_map)

        display = table[
            [
                "Rank",
                "symbol",
                "score",
                "grade",
                "decision",
                "confidence",
                "risk",
            ]
        ]

        # -------------------------------------------------
        # Search
        # -------------------------------------------------

        search = st.text_input(
            "🔍 Search Asset",
            placeholder="Example : RELIANCE",
        )

        if search:

            display = display[
                display["symbol"].str.contains(
                    search,
                    case=False,
                    na=False,
                )
            ]

        # -------------------------------------------------
        # Table
        # -------------------------------------------------

        st.dataframe(
            display,
            width="stretch",
            hide_index=True,
        )

        # -------------------------------------------------
        # Export
        # -------------------------------------------------

        csv = display.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Export Ranking",
            csv,
            file_name="RTDOS_Ranking.csv",
            mime="text/csv",
            width="stretch",
        )

        st.caption(f"Showing {len(display)} of {len(table)} assets.")
