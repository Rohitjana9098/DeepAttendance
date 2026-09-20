import streamlit as st

from src.UI.base_layout import style_background_home, style_base_layout
from src.components.header_home import (
    STUDENT_ICON_PATH,
    TEACHER_ICON_PATH,
    header_home,
)


def home_screen():
    # Styles are injected first so they apply to everything rendered below
    style_base_layout()
    style_background_home()

    # Branding + tagline (rendered before the buttons)
    header_home()

    # Portal cards: containers are created after the header,
    # so they render below it on screen
    col_teacher, col_student = st.columns(2, gap="large")

    with col_teacher:
        st.header("I'm Teacher")
        _, icon_col, _ = st.columns([1, 4, 1])
        with icon_col:
            if TEACHER_ICON_PATH.exists():
                st.image(str(TEACHER_ICON_PATH), width='stretch')
        if st.button(
            'Teacher Portal',
            key='home_teacher_btn',
            type='secondary',
            icon='🎓',
            width='stretch',
        ):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col_student:
        st.header("I'm Student")
        _, icon_col, _ = st.columns([1, 4, 1])
        with icon_col:
            if STUDENT_ICON_PATH.exists():
                st.image(str(STUDENT_ICON_PATH), width='stretch')
        if st.button(
            'Student Portal',
            key='home_student_btn',
            type='secondary',
            icon='🧑‍🎓',
            width='stretch',
        ):
            st.session_state['login_type'] = 'student'
            st.rerun()


