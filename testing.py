import streamlit as st

def inc_streak():
  st.session_state.streak = True
  try:
    with open(f"{st.user.email}strk.txt", "r+") as f:
      f.write("y")
  except FileNotFoundError:
    with open(f"{st.user.email}strk.txt", "w") as f:
      f.write("y")
def inc_score(x, y, streak, score):
  if x > y:
    if int(streak) == 0:
      st.session_state.score =  x - y
    else:
      st.session_state.score = (x - y) * (int(streak) / 10)
  elif x < y:
    if int(streak) == 0:
      if int(score) == 0:
        st.session_state.score = 0
      else:
        st.session_state.score = x - y
    else:
      st.session_state.score = (x - y) / (int(streak) / 10)
  elif x == y:
    st.session_state.score = 0

st.title("testing page")
