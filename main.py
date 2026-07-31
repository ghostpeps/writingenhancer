import streamlit as st

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
