import streamlit as st

st.title("Home")

if st.user.is_logged_in:
    st.write(f"Welcome {st.user.name}\nEmail: {st.user.email}")
else:
    st.info("Logged in without an account")

st.write("Welcome to your regular home page content!")

if st.button("Log out", icon=":material/log_out:"):
    if st.user.is_logged_in:
        st.logout()
    else:
        st.session_state.guest_mode = False
        st.rerun()
