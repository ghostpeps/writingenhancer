import streamlit as st
from google import genai
from google.genai import types

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

def d_complete(): # add percentage for different grades and incognito version
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

def ai_checker():
  if st.user.is_logged_in:
    with open(f"{st.user.email}grade.txt", "r") as f:
      grade = f.read().rstrip()
    if grade:
      g = grade[-1]
      
    gemini_api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=gemini_api_key)
    tutor_persona = (
    f"You are a patient, encouraging writing tutor for someone in {g} grade. Do not just rewrite "
    "the student's work. Instead, point out areas of improvement regarding structure, "
    "tone, and clarity. Provide concrete examples of how they can improve."
)
st.title("testing page")
