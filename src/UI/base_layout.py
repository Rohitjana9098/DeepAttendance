import streamlit as st


# Snap Class Lumina - Stitch redesign theme
# Source: src/UI/stitch_streamlit_ui_redesign/{code.html, DESIGN.md}

_LUMINA_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
.stApp, .stAppViewContainer, .stMain, .stMainBlockContainer, section.stMain > div {
    background-color: #faf8ff !important;
    background-image: radial-gradient(circle at 50% 0%, #e0e7ff 0%, #f8fafc 40%, #f1f5f9 100%) !important;
    background-attachment: fixed !important;
    font-family: 'Plus Jakarta Sans', -apple-system, 'Segoe UI', Roboto, sans-serif !important;
}
.stApp { color: #334155 !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 1rem !important; max-width: 64rem !important; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }
div[data-testid="stToolbar"], div[data-testid="stDecoration"] { visibility: hidden; }
h1 { font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 800 !important; letter-spacing: -0.025em !important; color: #0f172a !important; }
h2, h3, h4 { font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; color: #0f172a !important; }
p, span, label, div { font-family: 'Plus Jakarta Sans', sans-serif !important; }
[data-testid="stMarkdownContainer"] p { color: #475569 !important; }
.lumina-live-badge { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.9rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; background: rgba(255,255,255,0.8); border: 1px solid #e0e7ff; color: #4338ca !important; box-shadow: 0 2px 10px -1px rgba(99,102,241,0.15); }
.lumina-live-dot { width: 0.5rem; height: 0.5rem; border-radius: 9999px; background: #10b981; animation: lumina-pulse 1.6s ease-in-out infinite; }
@keyframes lumina-pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.45; } }
.lumina-logo { width: 3rem; height: 3rem; border-radius: 1rem; background: linear-gradient(135deg, #4f46e5 0%, #6366f1 50%, #8b5cf6 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px -4px rgba(99,102,241,0.45); font-size: 1.5rem; }
.lumina-brand-title { font-size: 2.25rem; font-weight: 800; letter-spacing: -0.03em; color: #0f172a !important; margin: 0 !important; line-height: 1.1 !important; }
.lumina-tagline { color: #64748b !important; font-size: 1rem !important; margin-top: 0.35rem !important; }
[data-testid="stColumn"] > div { background: rgba(255,255,255,0.92) !important; backdrop-filter: blur(16px) !important; border: 1px solid #e2e8f0 !important; border-radius: 1.5rem !important; box-shadow: 0 10px 25px -5px rgba(99,102,241,0.08) !important; padding: 1.6rem !important; }
[data-testid="stColumn"] > div:hover { border-color: rgba(99,102,241,0.35) !important; box-shadow: 0 20px 35px -8px rgba(99,102,241,0.16) !important; }
[data-testid="stColumn"] h2 { font-size: 1.5rem !important; color: #0f172a !important; margin-bottom: 0.25rem !important; }
.lumina-card-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.1rem; }
.lumina-icon-box { width: 3rem; height: 3rem; border-radius: 1rem; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; }
.lumina-icon-indigo { background: #eef2ff; border: 1px solid #e0e7ff; }
.lumina-icon-sky { background: #f0f9ff; border: 1px solid #e0f2fe; }
.lumina-role-tag { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; padding: 0.25rem 0.65rem; border-radius: 0.5rem; border: 1px solid; }
.lumina-role-faculty { color: #4338ca !important; background: #eef2ff; border-color: #e0e7ff; }
.lumina-role-scholar { color: #0369a1 !important; background: #f0f9ff; border-color: #e0f2fe; }
.lumina-card-title { font-size: 1.5rem !important; font-weight: 700 !important; color: #0f172a !important; margin: 0 0 0.4rem 0 !important; }
.lumina-card-desc { font-size: 0.875rem !important; color: #64748b !important; margin-bottom: 1.1rem !important; line-height: 1.55 !important; }
.lumina-feats { list-style: none !important; padding: 0 !important; margin: 0 0 1.4rem 0 !important; }
.lumina-feats li { display: flex; align-items: center; gap: 0.5rem; font-size: 0.78rem !important; color: #334155 !important; font-weight: 500; margin-bottom: 0.6rem !important; }
.lumina-check { color: #059669 !important; font-weight: 800; }
div.stButton > button { width: 100%; border-radius: 0.75rem !important; font-weight: 600 !important; font-size: 0.875rem !important; padding: 0.75rem 1rem !important; }
div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important; color: #fff !important; border: none !important; box-shadow: 0 4px 12px rgba(99,102,241,0.25) !important; }
div.stButton > button[kind="primary"]:hover { filter: brightness(1.06) !important; color: #fff !important; }
div.stButton > button[kind="primary"] p { color: #fff !important; }
div.stButton > button[kind="secondary"] { background: #f8fafc !important; color: #334155 !important; border: 1px solid #e2e8f0 !important; }
div.stButton > button[kind="secondary"]:hover { background: #f1f5f9 !important; border-color: #cbd5e1 !important; color: #0f172a !important; }
div.stButton > button[kind="secondary"] p { color: inherit !important; }
div.stButton > button[kind="tertiary"] { background: transparent !important; color: #334155 !important; }
[data-testid="stMetric"] { background: rgba(255,255,255,0.92) !important; border: 1px solid #e2e8f0 !important; border-radius: 1rem !important; padding: 1rem 1.2rem !important; }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.85) !important; border-right: 1px solid #e2e8f0 !important; }
.lumina-pill { display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.2rem 0.7rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 600; border: 1px solid #e2e8f0; background: rgba(255,255,255,0.9); color: #475569 !important; }
.lumina-footer { text-align: center; padding: 1.2rem 1rem 0.3rem 1rem; }
.lumina-footer small { color: #94a3b8 !important; font-size: 0.75rem; }
a { color: #4f46e5 !important; }
</style>
"""


def style_base_layout():
    st.markdown(_LUMINA_CSS, unsafe_allow_html=True)


def style_background_home():
    st.markdown("<style>.stApp{background-color:#faf8ff !important;}</style>", unsafe_allow_html=True)


def style_background_dashboard():
    style_background_home()


def style_portal_cards():
    return None

