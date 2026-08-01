import streamlit as st
from datetime import datetime

if not st.user.is_logged_in or st.session_state.guest_mode:
    st.title("Welcome to the English Tutor")
    st.write("Please log in or practice without an account to access the tutor.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign in with Google", icon=":material/account_circle:", use_container_width=True):
            st.login()
    
    with col2:
        guestbtn = st.button("Practice without an account", icon=":material/account_circle_off:", use_container_width=True)
        st.caption("Note that by clicking this button you will be automatically logged out within 24 hours")
        if guestbtn:
            st.session_state.guest_mode = True
            st.session_state.guest_login_time = datetime.now()
            st.rerun()
elif st.user.is_logged_in or st.session_state.guest_mode:
    grade = st.selectbox("Please choose your grade:", ("1", "2", "3", "4", "5", "6"), None)
    if st.button("Submit", ":material/send:"):
        st.session_state.selected_grade = True
        st.rerun()
