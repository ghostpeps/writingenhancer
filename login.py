import streamlit as st

st.title("🔒 Welcome to the App")
st.write("Please log in or continue as a guest to access the dashboard.")

# Column layout for side-by-side buttons
col1, col2 = st.columns(2)

with col1:
    # Native Streamlit OIDC login trigger
    if st.button("🚀 Sign in with Google", use_container_width=True):
        st.login() # Redirects to Google authentication screen

with col2:
    # Guest option bypasses Google but flags the session state
    if st.button("📝 Practice without an account", use_container_width=True):
        st.session_state.guest_mode = True
        st.rerun()
