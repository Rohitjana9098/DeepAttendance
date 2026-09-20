from pathlib import Path

import streamlit as st

_ASSETS = Path(__file__).parent.parent / "UI" / "assets"
ICON_PATH = _ASSETS / "attendance_icon.png"
TEACHER_ICON_PATH = _ASSETS / "teacher_icon.png"
STUDENT_ICON_PATH = _ASSETS / "student_icon.png"


def header_home():
    st.markdown(
        """
        <style>
        /* Brand title on the home screen */
        .home-brand {
            font-family: 'Archivo Black', sans-serif !important;
            color: #ffffff !important;
            text-align: center !important;
            margin-bottom: 0.25rem !important;
        }

        /* Tagline under the brand title */
        .home-tagline {
            font-family: 'Jost', sans-serif !important;
            color: #F3E3F0 !important;
            font-size: 1.25rem !important;
            text-align: center !important;
            margin-bottom: 2.5rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Hero icon, centered
    if ICON_PATH.exists():
        _, img_col, _ = st.columns([1, 1, 1])
        with img_col:
            st.image(str(ICON_PATH), width=200)

    st.markdown(
        """
        <h1 class='home-brand'>&#128248; Snap Class</h1>
        <p class='home-tagline'>AI-powered attendance, one snap at a time.</p>
        """,
        unsafe_allow_html=True,
    )