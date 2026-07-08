"""
RT-DOS Intelligence Platform
Module      : Theme Engine
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

from dataclasses import dataclass
import streamlit as st

# ==========================================================
# Theme Model
# ==========================================================


@dataclass(frozen=True)
class Theme:

    name: str

    background: str
    secondary_background: str

    primary: str
    secondary: str

    success: str
    warning: str
    danger: str
    info: str

    text: str
    muted_text: str

    border: str

    card_radius: int
    spacing: int


# ==========================================================
# RT-DOS Themes
# ==========================================================

LIGHT_PRO = Theme(
    name="Light Professional",
    background="#FFFFFF",
    secondary_background="#F7F8FA",
    primary="#0A84FF",
    secondary="#2D3748",
    success="#16A34A",
    warning="#F59E0B",
    danger="#DC2626",
    info="#2563EB",
    text="#111827",
    muted_text="#6B7280",
    border="#E5E7EB",
    card_radius=14,
    spacing=16,
)


DARK_TRADER = Theme(
    name="Dark Trader",
    background="#0F172A",
    secondary_background="#1E293B",
    primary="#3B82F6",
    secondary="#CBD5E1",
    success="#22C55E",
    warning="#FBBF24",
    danger="#EF4444",
    info="#60A5FA",
    text="#F8FAFC",
    muted_text="#94A3B8",
    border="#334155",
    card_radius=14,
    spacing=16,
)


SLATE_GREY = Theme(
    name="Slate Grey",
    background="#ECEFF3",
    secondary_background="#DDE2E8",
    primary="#2563EB",
    secondary="#334155",
    success="#16A34A",
    warning="#D97706",
    danger="#DC2626",
    info="#2563EB",
    text="#0F172A",
    muted_text="#64748B",
    border="#CBD5E1",
    card_radius=14,
    spacing=16,
)


# ==========================================================
# Theme Registry
# ==========================================================

THEMES = {
    "Light Professional": LIGHT_PRO,
    "Dark Trader": DARK_TRADER,
    "Slate Grey": SLATE_GREY,
}


# ==========================================================
# Theme Selection
# ==========================================================


def get_theme():

    if "theme" not in st.session_state:
        st.session_state.theme = "Light Professional"

    return THEMES[st.session_state.theme]


def set_theme(name: str):

    if name in THEMES:
        st.session_state.theme = name


# ==========================================================
# Theme Selector
# ==========================================================


def theme_selector():

    current = st.session_state.get(
        "theme",
        "Light Professional",
    )

    selected = st.selectbox(
        "Theme",
        options=list(THEMES.keys()),
        index=list(THEMES.keys()).index(current),
        key="theme_selector",
    )

    if selected != current:

        st.session_state.theme = selected

        st.rerun()


# ==========================================================
# Global Styling
# ==========================================================


def apply_theme():

    theme = get_theme()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-color: {theme.background};
            color: {theme.text};
        }}

        div[data-testid="stMetric"] {{
            background: {theme.secondary_background};
            border: 1px solid {theme.border};
            border-radius: {theme.card_radius}px;
            padding: 12px;
        }}

        div[data-testid="stDataFrame"] {{
            border-radius: {theme.card_radius}px;
        }}

        h1,h2,h3,h4,h5,h6 {{
            color: {theme.text};
        }}

        hr {{
            border-color: {theme.border};
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# Colour Helpers
# ==========================================================


def success_colour():

    return get_theme().success


def warning_colour():

    return get_theme().warning


def danger_colour():

    return get_theme().danger


def info_colour():

    return get_theme().info


def primary_colour():

    return get_theme().primary


def text_colour():

    return get_theme().text
