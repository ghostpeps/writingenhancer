import streamlit as st

def home():
    st.title("Home")
    st.write("Welcome!")

def analytics():
    st.title("Analytics")
    st.write("Data insights.")

pg = st.navigation([
    st.Page(home, title="Home", icon=":material/home:"),
    st.Page(analytics, title="Analytics", icon=":material/bar_chart:")
])
pg.run()
