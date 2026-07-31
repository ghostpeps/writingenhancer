import streamlit as st

pg = st.navigation([
    st.Page("home.py", title="Home", icon=":material/home:"),
    st.Page("data.py", title="Data", icon=":material/bar_chart:")
])
pg.run()
