"""
RT-DOS Intelligence Platform
Module      : Market Pulse Card
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

import plotly.graph_objects as go
import streamlit as st

from ui.theme import get_theme


def show_market_health(score):

    theme = get_theme()

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "%"},
            title={"text": "Market Health"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": theme.primary},
                "steps": [
                    {
                        "range": [0, 30],
                        "color": "#E53935",
                    },
                    {
                        "range": [30, 60],
                        "color": "#FB8C00",
                    },
                    {
                        "range": [60, 80],
                        "color": "#43A047",
                    },
                    {
                        "range": [80, 100],
                        "color": "#00C853",
                    },
                ],
            },
        )
    )

    fig.update_layout(
        height=280,
        margin=dict(
            l=10,
            r=10,
            t=50,
            b=10,
        ),
        paper_bgcolor=theme.background,
        plot_bgcolor=theme.background,
        font=dict(
            color=theme.text,
            size=14,
        ),
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )
