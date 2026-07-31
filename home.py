import streamlit as st

st.title("🏡 Main Dashboard")

# Customize greeting based on how they entered the app
if st.user.is_logged_in:
    st.success(f"Logged in via Google as: {st.user.name} ({st.user.email})")
else:
    st.info("Browsing in Guest Mode (Practice)")

st.write("Welcome to your regular home page content!")

# Provide a clean exit option to return to the landing page
if st.button("Exit / Log Out"):
    if st.user.is_logged_in:
        st.logout()
    else:
        st.session_state.guest_mode = False
        st.rerun()
