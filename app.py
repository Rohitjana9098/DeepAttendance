import streamlit as st
from src.screen.home_screen import home_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_screen import teacher_screen

def main():
    if "login_type" not in st.session_state:
        home_screen()
    else:
        match st.session_state['login_type']:
            case "teacher":
                teacher_screen()
            case "student":
                student_screen()
            case None | _:
                home_screen()

if __name__ == "__main__":
    main()