import streamlit as st
from datetime import date

if "guest_mode" not in st.session_state:
    st.session_state.guest_mode = False

if "guest_login_date" not in st.session_state:
    st.session_state.guest_login_date = None

if st.session_state.guest_mode and st.session_state.guest_login_date:
    if date.today() > st.session_state.guest_login_date:
        st.session_state.guest_mode = False
        st.session_state.guest_login_date = None
        st.rerun()

if "guest_mode" not in st.session_state:
    st.session_state.guest_mode = False

if st.user.is_logged_in or st.session_state.guest_mode:
    pages = [
        st.Page("home.py", title="Home", icon=":material/home:", default=True),
        st.Page("data.py", title="Data", icon=":material/bar_chart:")
    ]
else:
    pages = [
        st.Page("login.py", title="Login", icon=":material/login:", default=True)
    ]

pg = st.navigation(pages)
pg.run()
