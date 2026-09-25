from pathlib import Path

import streamlit as st

_ASSETS = Path(__file__).parent.parent / "UI" / "assets"
ICON_PATH = _ASSETS / "attendance_icon.png"
TEACHER_ICON_PATH = _ASSETS / "teacher_icon.png"
STUDENT_ICON_PATH = _ASSETS / "student_icon.png"


def header_home():
    st.markdown(
        "<div style='text-align:center; padding-top:1.2rem;'>"
        "<span class='lumina-live-badge'>"
        "<span class='lumina-live-dot'></span>"
        "AI Facial Recognition v2.4 Active</span></div>",
        unsafe_allow_html=True,
    )
    if ICON_PATH.exists():
        _, img_col, _ = st.columns([3, 2, 3])
        with img_col:
            st.markdown("<div class='lumina-logo'>&#128248;</div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align:center; padding: 0.4rem 0 0.2rem 0;'>"
        "<p class='lumina-brand-title'>Snap Class</p>"
        "<p class='lumina-tagline'>Smart automatic attendance, powered by "
        "real-time neural vision. One snap at a time.</p></div>",
        unsafe_allow_html=True,
    )
