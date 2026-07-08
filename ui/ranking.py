"""
RT-DOS Intelligence Platform
Ranking Panel
Version : 2.0.0
"""

import pandas as pd
import streamlit as st


class RankingPanel:

    def show(self, ranked):

        st.subheader("🏆 Market Intelligence Ranking")

        st.caption("Assets ranked by RT-DOS Composite Intelligence")

        if not ranked:
            st.warning("No ranking data available.")
            return

        table = pd.DataFrame(ranked)

        columns = [
            "symbol",
            "score",
            "grade",
            "decision",
            "confidence",
            "risk",
        ]

        table = table[columns]

        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True,
        )
