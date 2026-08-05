import streamlit as st
from datetime import datetime, timedelta

if st.user.is_logged_in:
  if st.user.given_name[-1] == "s":
    st.title(f"{st.user.given_name}' Test Data")
  else:
    st.title(f"{st.user.given_name}'s Test Data")
else:
  st.title("Test Data")
if not st.user.is_logged_in:
  st.write("View test data from today, including areas to improve on, here.")
else:
  st.write("View test data, including tests and areas to improve on, here.")

if st.user.is_logged_in:
  s1, s2 = st.sidebar.columns(2, vertical_alignment="center")
  with s1:
    try:
        with open(f"{st.user.email}strk.txt", "r") as f:
            v = f.read()
    except FileNotFoundError:
        with open(f"{st.user.email}strk.txt", "w") as f:
            f.write("n")
            v = "n"
    try:
        with open(f"{st.user.email}streak.txt", "r") as f:
            u = f.read()
    except FileNotFoundError:
        with open(f"{st.user.email}streak.txt", "w") as f:
            f.write("0")
            u = "0"
    if v == "y":
      with open(f"{st.user.email}streak.txt", "r+") as f:
          z = f.read()
      st.markdown(":color[:material/mode_heat:" + z + "]{foreground='#fa3002'}")
    elif v == "n" and u != "0":
        try:
            with open(f"{st.user.email}streak.txt", "r") as f:
                z = f.read()
        except FileNotFoundError:
            with open(f"{st.user.email}streak.txt", "w") as f:
                z = 0
        st.markdown(":color[:material/mode_heat: " + z + "]{foreground='#f0ab18'}")
    elif u == "0":
        st.markdown(":color[:material/mode_heat: 0]{foreground='#827f6c'}")
  with s2:
    @st.dialog("Test Score", dismissible=True)
    def show_popup_message(message_text):
        st.write(message_text)
    with open(f"{st.user.email}score.txt", "r+") as f:
        w = f.read()
    if st.button(f"{w}", type="tertiary", use_container_width=True):
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

