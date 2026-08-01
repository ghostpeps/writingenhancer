import streamlit as st
from datetime import datetime, timedelta

st.title("Home")

if st.user.is_logged_in:
    st.write(f"Welcome {st.user.name}\nEmail: {st.user.email}")
else:
    st.write("Logged in without an account")

st.header("Tests:")
if not st.session_state.selected_grade:
    grade = st.selectbox("Please choose your grade to start testing", ("1", "2", "3", "4", "5", "6"), None)
    if grade:
        st.session_state.selected_grade = True
        st.rerun()
elif st.session_state.selected_grade:
    st.write("Tests will be here")
    
with st.sidebar:
    if st.session_state.get("guest_mode") and st.session_state.get("guest_login_time"):
        start_time = st.session_state.guest_login_time
        expiration_time = start_time + timedelta(hours=24)
        current_time = datetime.now()
        time_left = expiration_time - current_time
        total_seconds = int(time_left.total_seconds())
        
        if total_seconds > 0:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            st.metric(label="Time until automatically logged out:", value=f"{hours}:{minutes}")
        else:
            st.error("Session expired! Refreshing...")
        
    if st.button("Log Out", icon=":material/logout:", use_container_width=True):
        st.session_state.guest_mode = False
        st.session_state.guest_login_time = None
        
        if st.user.is_logged_in:
            st.logout()
        else:
            st.rerun()
