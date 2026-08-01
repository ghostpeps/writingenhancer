import streamlit as st
from datetime import datetime, timedelta

col1, col2 = st.columns(2)

with col1:
    st.title("Home")
    
    if st.user.is_logged_in:
        st.write(f"Welcome, {st.user.name}\nEmail: {st.user.email}")
    else:
        st.write("Logged in without an account")

with col2:
    st.title("Tests")
    if not st.session_state.selected_grade:
        grade = st.selectbox("Please choose your grade to start testing", ("1", "2", "3", "4", "5", "6"), None)
        if grade:
            st.session_state.selected_grade = True
            st.rerun()
    elif st.session_state.selected_grade:
        st.write("Tests will be here")

if st.user.is_logged_in:
    s1, s2 = st.colomns(2)
    with s1:
        st.sidebar.markdown(":material/mode_heat: Some Number") #add one to streak every time submit button is clicked in test. add html to make streak logo and text. save to file
    with s2:
        @st.dialog("Test Score", dismissible=True)
        def show_popup_message(message_text):
            st.write(message_text)
        if st.sidebar.button("Some Number", type="Tertiary"): #save to file. make sure to add/subtract to/from score
            show_popup_message("The test score is used to define your overall improvements. The more positive feedback you receive, the higher your score goes, and the more negative feedback you receive, the lower your score goes. Your streak also affects your test score. If your streak is higher, your score will increase faster, while reducing the amount you decrease when given negative feedback. ")
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
