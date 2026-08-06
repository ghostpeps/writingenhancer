import streamlit as st

try:
  with open(f"{st.user.email}strk.txt", "r") as f:
    a = f.read()
except FileNotFoundError:
  with open(f"{st.user.email}strk.txt", "w") as f:
    f.write("n")
    a = "n"
if a == "n":
  st.subheader("Complete at least one test today to play games")
  if st.button("Go to Tests", icon=":material/assignment:"):
    st.switch_page("home.py") 
elif a == "y":
  st.title("Games")
