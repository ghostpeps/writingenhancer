import streamlit as st
from datetime import datetime, timedelta

if "guest_mode" not in st.session_state:
    st.session_state.guest_mode = False

if "guest_login_time" not in st.session_state:
    st.session_state.guest_login_time = None

def manual_logout():
    st.session_state.guest_mode = False
    st.session_state.guest_login_time = None
    if st.user.is_logged_in:
        st.logout()
    else:
        st.rerun()
if st.session_state.guest_mode and st.session_state.guest_login_time:
    if datetime.now() > (st.session_state.guest_login_time + timedelta(hours=24)):
        manual_logout()
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
