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

def ai_checker(writing):
  if st.user.is_logged_in:
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
    if z == "100":
      gemini_api_key = st.secrets["GEMINI_API_KEY"]
      client = genai.Client(api_key=gemini_api_key)
      tutor_persona = (
        f"You are a strict, helpful writing tutor for a student in {g} grade. Your output must strictly follow these rules:\n"
        "1. Every single point you make must be a bullet point (•).\n"
        "2. Every bullet point must explicitly start with either '• Positive: ' or '• Negative: ' followed by your feedback.\n"
        "3. Quote specific examples from the student's text to explain your points (e.g., 'at \"The lion followed the tiger, slowly\" you forgot to add a period.').\n"
        "Do not include any introductory or concluding text. Only provide the requested bullet points."
        )
        full_prompt = (
          f"Please evaluate this writing:\n"
          f"\"\"\"\n{writing}\n\"\"\""
        )
        try:
          api_call = client.models.generate_content(
              model='gemini-1.5-flash',
              contents=full_prompt,
              config=types.GenerateContentConfig(
                  system_instruction=tutor_persona,
                  temperature=0.3,
              )
          )
          response = api_call.text
      
        except Exception as e:
            response = "Error generating feedback."
            st.error(f"An error occurred: {e}. Please try again.")
  
        return response
      elif z != "100": # add more stuff for diognostics
        pass
st.title("testing page")
