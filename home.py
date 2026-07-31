import streamlit as st

st.title("Main Dashboard")

if st.user.is_logged_in:
    st.success(f"Logged in via Google as: {st.user.name} ({st.user.email})")
else:
    st.info("Browsing in Guest Mode (Practice)")

st.write("Welcome to your regular home page content!")

if st.button("Exit / Log Out"):
    if st.user.is_logged_in:
        st.logout()
    else:
        st.session_state.guest_mode = False
        st.rerun()
