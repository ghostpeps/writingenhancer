import streamlit as st
from datetime import datetime, timedelta

col1, col2 = st.columns(2)

with col1:
    st.title("Home")
    
    if st.user.is_logged_in:
        st.write(f"Welcome, {st.user.name}")
        st.write(f"Email: {st.user.email}")
        st.write(f"Preferred Language: {st.context.locale}")
    else:
        st.write("Logged in without an account")

with col2:
    st.title("Tests")
    if not st.session_state.selected_grade:
        grade = st.selectbox("Please choose your grade to start testing", ("1", "2", "3", "4", "5", "6"), None)
        if grade:
            with open(f"{st.user.email}.txt", "a", encoding="utf-8") as f:
                f.write(f"Grade: {grade}")
            st.session_state.selected_grade = True
            st.rerun()
    elif st.session_state.selected_grade:
        grade = st.selectbox("Change Grade", ("1", "2", "3", "4", "5", "6"), None)
        if grade:
            with open(f"{st.user.email}.txt", "rb+") as f:
                f.seek(5, 0)
                x = f"{grade}"
                f.write(x.encode("utf-8"))
        st.write("Tests will be here")
        with open(f"{st.user.email}.txt", "r", encoding="utf-8") as f:
            st.write(f.read())
if st.user.is_logged_in:
    s1, s2 = st.sidebar.columns(2, vertical_alignment="center")
    with s1:
        st.markdown(":material/mode_heat: 0") #add one to streak every time submit button is clicked in test. add html to make streak logo and text. save to file
    with s2:
        @st.dialog("Test Score", dismissible=True)
        def show_popup_message(message_text):
            st.write(message_text)
        if st.button("0", type="tertiary", use_container_width=True): #save to file. make sure to add/subtract to/from score
            show_popup_message("The test score is used to define your overall improvements. The more positive feedback you receive, the higher your score goes, and the more negative feedback you receive, the lower your score goes. Your streak also affects your test score. If your streak is higher, your score will increase faster, while reducing the amount you decrease when given negative feedback. Complete a test every day (including diagnostics) to increase your streak. If you forget to test for just one day, your streak restarts at 0.")
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
