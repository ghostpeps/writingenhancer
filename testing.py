import streamlit as st

def inc_streak():
  try:
    with open(f"{st.user.email}strk.txt", "r+") as f:
      f.write("y")
  except FileNotFoundError:
    with open(f"{st.user.email}strk.txt", "w") as f:
      f.write("y")
def inc_score(x, y):
  try:
    with open(f"{st.user.email}streak.txt", "r") as f:
      z = f.read()
  except FileNotFoundError:
    with open(f"{st.user.email}streak.txt", "w") as f:
      f.write("0")
      z = "0"
  try:
    with open(f"{st.user.email}score.txt", "r") as f:
      w = f.read()
  except FileNotFoundError:
    with open(f"{st.user.email}score.txt", "w") as f:
      f.write("0")
      w = "0"
  with open(f"{st.user.email}score.txt", "w") as f:
    if x > y:
      if int(z) == 0:
        f.write(str(int(w)+(x-y)))
      else:
        f.write(str(int(w)+((x - y) * (int(z) / 10))))
    elif x < y:
      if int(z) == 0:
        if int(w) == 0:
          f.write(w)
        else:
          f.write(str(int(w)+(x-y)))
      else:
        f.write(str(int(w)+((x - y) / (int(z) / 10))))
    elif x == y:
      f.write(w)

def d_complete(): # add percentage for different grades
  try:
    with open(f"{st.user.email}d.txt", "r") as f:
      z = f.read()
  except FileNotFoundError:
    with open(f"{st.user.email}d.txt", "w") as f:
      f.write("0")
      z = "0"
  with open(f"{st.user.email}grade.txt", "r") as f:
    grade = f.read().rstrip()
    if grade:
      g = grade[-1]
st.title("testing page")
