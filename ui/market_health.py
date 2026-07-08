import plotly.graph_objects as go
import streamlit as st


def show_market_health(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "%"},
            title={"text": "Market Health"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#00C853"},
                "steps": [
                    {"range": [0, 30], "color": "#8B0000"},
                    {"range": [30, 60], "color": "#FFB300"},
                    {"range": [60, 80], "color": "#43A047"},
                    {"range": [80, 100], "color": "#00C853"},
                ],
            },
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor="#0E1117",
        font={"color": "white"},
    )

    st.plotly_chart(fig, use_container_width=True)
