import streamlit as st

st.title("Welcome to the English Tutor")
st.write("Please log in or continue without an account to access the tutor.")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sign in with Google", icon=":material/account_circle:", use_container_width=True):
        st.login()

with col2:
    guestbtn = st.button("Practice without an account", icon=":material/account_circle_off:", use_container_width=True)
    st.write("Note that by clicking this button you will be automatically logged out within 24 hours")
    if guestbtn:
        st.session_state.guest_mode = True
        st.rerun()
