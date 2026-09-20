import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            /* Home background */
            .stApp, .stAppViewContainer, .stMain,
            .stMainBlockContainer, .stAppHeader, section.stMain > div {
                background: #191851 !important;
                background-color: #191851 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            /* Dashboard background */
            .stApp {
                background: #191851 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Jost:ital,wght@0,100..900;1,100..900&display=swap');

        /* =========================================
           HIDE STREAMLIT DEFAULT UI
        ========================================= */

        #MainMenu, footer, header {
            visibility: hidden;
        }


        /* =========================================
           PAGE SPACING
        ========================================= */

        .block-container {
            padding-top: 1.5rem !important;
        }


        /* =========================================
           H1 - BRAND TITLE
           Pure White: #FFFFFF
        ========================================= */

        h1 {
            font-family: 'Archivo Black', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0.5rem !important;
            color: #FFFFFF !important;
        }


        /* =========================================
           H2
           Pure White: #FFFFFF
        ========================================= */

        h2 {
            font-family: 'Jost', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0.5rem !important;
            color: #FFFFFF !important;
        }


        /* =========================================
           OTHER TEXT
           Cool Slate: #94A3B8
        ========================================= */

        h3, h4, p, span {
            font-family: 'Jost', sans-serif !important;
        }

        h3, h4 {
            color: #FFFFFF !important;
        }

        p {
            color: #94A3B8 !important;
        }


        /* =========================================
           PRIMARY BUTTON
           Amber + Charcoal Navy
        ========================================= */

        button[kind="primary"] {
            border-radius: 1.5rem !important;
            background: #F59E0B !important;
            color: #1E293B !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: background-color 0.3s ease-in-out !important;
        }

        button[kind="primary"]:hover {
            background: #FBBF24 !important;
            color: #1E293B !important;
        }


        /* =========================================
           SECONDARY BUTTON
           Navy + Amber outline
        ========================================= */

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background: #191851 !important;
            color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: 2px solid #F59E0B !important;
            transition: background-color 0.3s ease-in-out !important;
        }

        button[kind="secondary"]:hover {
            background: #F59E0B !important;
            color: #1E293B !important;
            border: 2px solid #F59E0B !important;
        }


        /* =========================================
           TERTIARY BUTTON
           Charcoal Navy + White
        ========================================= */

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background: #1E293B !important;
            color: #FFFFFF !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: background-color 0.3s ease-in-out !important;
        }

        button[kind="tertiary"]:hover {
            background: #334155 !important;
            color: #FFFFFF !important;
        }


        /* =========================================
           NAVIGATION / SECONDARY LINKS
           Cool Slate
        ========================================= */

        a {
            color: #94A3B8 !important;
        }

        a:hover {
            color: #FFFFFF !important;
        }


        /* =========================================
           FOOTER / SECONDARY META TEXT
           Muted Steel
        ========================================= */

        .footer,
        .secondary-text {
            color: #64748B !important;
        }


        /* =========================================
           BIOMETRIC SECURITY LIVE STATUS
           Emerald Green indicator
        ========================================= */

        .live-status {
            color: #FFFFFF !important;
            font-family: 'Jost', sans-serif !important;
        }

        .live-dot {
            color: #10B981 !important;
            font-size: 14px !important;
        }


        </style>
    """, unsafe_allow_html=True)

