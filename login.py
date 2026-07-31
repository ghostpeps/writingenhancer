import streamlit as st
from datetime import datetime
import pytz
from streamlit_js_eval import streamlit_js_eval

st.title("Welcome to the English Tutor")
st.write("Please log in or continue without an account to access the tutor.")

col1, col2 = st.columns(2)

user_timezone_str = streamlit_js_eval(data_element="Intl.DateTimeFormat().resolvedOptions().timeZone", key="tz")

with col1:
    if st.button("Sign in with Google", icon=":material/account_circle:", use_container_width=True):
        st.login()

with col2:
    guestbtn = st.button("Practice without an account", icon=":material/account_circle_off:", use_container_width=True)
    st.caption("Note that by clicking this button you will be automatically logged out within 24 hours")
    if guestbtn:
        st.session_state.guest_mode = True
        if user_timezone_str:
            user_tz = pytz.timezone(user_timezone_str)
            st.session_state.user_timezone = user_timezone_str
        else:
            user_tz = pytz.utc
            st.session_state.user_timezone = "UTC"
            
        st.session_state.guest_login_time = datetime.now(user_tz) 
        st.rerun()
