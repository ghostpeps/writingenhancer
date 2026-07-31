import streamlit as st
from datetime import timedelta

st.title("Home")

if st.user.is_logged_in:
    st.write(f"Welcome {st.user.name}\nEmail: {st.user.email}")
else:
    st.info("Logged in without an account")

if st.button("Log out", icon=":material/logout:"):
    if st.user.is_logged_in:
        st.logout()
    else:
        st.session_state.guest_mode = False
        st.rerun()

with st.sidebar:
    if st.session_state.get("guest_mode"):
        end_time = st.session_state.guest_login_time + timedelta(hours=24)
        end_string = end_time.strftime("%b %d, at %I:%M %p")
      
        login_string = st.session_state.guest_login_time.strftime("%I:%M %p")
        st.caption(f"Guest session started at {login_string}. You have until {end_string} before you get logged out.")
        
    if st.button("Log Out", icon=":material/logout:", use_container_width=True):
        st.session_state.guest_mode = False
        st.session_state.guest_login_time = None
        
        if st.user.is_logged_in:
            st.logout()
        else:
            st.rerun()
