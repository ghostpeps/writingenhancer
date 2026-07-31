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
