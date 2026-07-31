import streamlit as st

st.title("Welcome to the English Tutor")
st.write("Please log in or continue without an account to access the tutor.")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sign in with Google", use_container_width=True):
        st.login()

with col2:
    if st.button("Practice without an account", use_container_width=True):
        st.session_state.guest_mode = True
        st.rerun()
