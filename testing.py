import streamlit as st

def inc_streak(x):
  x = True
  return x

def inc_score(x, y, streak, score):
  if x > y:
    if int(streak) == 0:
      return x - y
    else:
      return (x - y) * int(streak) / 10
  elif x < y:
    if int(streak) == 0:
      if int(score) == 0:
        return 0
      else:
        return x - y
    else:
      return (x - y) / int(streak) / 10
  elif x == y:
    return 0

st.title("testing page")
