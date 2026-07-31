import streamlit as st

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
    st.write("---")

    if st.session_state.get("guest_mode"):
        login_string = st.session_state.guest_login_time.strftime("%I:%M %p")
        st.caption(f"⏱️ Guest session started at: {login_string}")
        
    if st.button("🚪 Log Out / Exit", use_container_width=True):
        st.session_state.guest_mode = False
        st.session_state.guest_login_time = None
        
        if st.user.is_logged_in:
            st.logout()
        else:
            st.rerun()
