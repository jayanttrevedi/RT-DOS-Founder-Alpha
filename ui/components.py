"""
RT-DOS Intelligence Platform
Module      : UI Components
Version     : 1.0.0
Status      : Production
Architecture: Design System
"""

import streamlit as st

# ==========================================================
# Section Header
# ==========================================================


class SectionHeader:

    @staticmethod
    def show(title, subtitle=""):

        st.subheader(title)

        if subtitle:
            st.caption(subtitle)


# ==========================================================
# Status Card
# ==========================================================


class StatusCard:

    @staticmethod
    def show(label, value, delta=None):

        st.metric(
            label=label,
            value=value,
            delta=delta,
        )


# ==========================================================
# Signal Badge
# ==========================================================


class SignalBadge:

    COLOURS = {
        "STRONG BUY": "🟢",
        "BUY": "🟢",
        "WATCH": "🟡",
        "HOLD": "🟠",
        "SELL": "🔴",
        "AVOID": "🔴",
    }

    @classmethod
    def show(cls, signal):

        icon = cls.COLOURS.get(signal, "⚪")

        st.markdown(f"### {icon} {signal}")


# ==========================================================
# Risk Badge
# ==========================================================


class RiskBadge:

    COLOURS = {
        "LOW": "🟢",
        "MEDIUM": "🟡",
        "HIGH": "🔴",
    }

    @classmethod
    def show(cls, risk):

        icon = cls.COLOURS.get(risk, "⚪")

        st.markdown(f"**Risk : {icon} {risk}**")


# ==========================================================
# Information Panel
# ==========================================================


class InfoPanel:

    @staticmethod
    def show(title, body):

        with st.container():

            st.markdown(f"### {title}")

            st.write(body)


# ==========================================================
# Divider
# ==========================================================


class Divider:

    @staticmethod
    def show():

        st.divider()
