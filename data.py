import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go

if st.user.is_logged_in:
  if st.user.given_name[-1] == "s":
    st.title(f"{st.user.given_name}' Test Data")
  else:
    st.title(f"{st.user.given_name}'s Test Data")
else:
  st.title("Test Data")
if not st.user.is_logged_in:
  st.write("View test data from today, including areas to improve on, here.")
else:
  st.write("View test data, including tests and areas to improve on, here.")


if st.user.is_logged_in:
    try:
        with open(f"{st.user.email}d.txt", "r") as f:
            progress_value = int(f.read())
    except FileNotFoundError:
        with open(f"{st.user.email}d.txt", "w") as f:
            f.write("0")
            progress_value = 0
    if progress_value != 100:
        filled_part = (progress_value / 100) * 250
        empty_part = 250 - filled_part
        hidden_bottom = 110
        fig = go.Figure(
            data=[
                go.Pie(
                    values=[filled_part, empty_part, hidden_bottom],
                    rotation=237, 
                    direction="clockwise",
                    hole=0.8,
                    marker=dict(
                        colors=["#FF4B4B", "#E5E5E5", "rgba(0,0,0,0)"]
                    ),
                    hoverinfo="skip",
                    textinfo="none",
                    sort=False,
                )
            ]
        )
        
        fig.update_layout(
            annotations=[
                dict(
                    text=f"{progress_value}%",
                    x=0.5,
                    y=0.5,
                    font_size=42,
                    font_weight="bold",
                    showarrow=False,
                ),
                dict(
                    text="Diagnostic Progress",
                    x=0.5,
                    y=0.3,
                    font_size=14,
                    font_color="gray",
                    showarrow=False,
                )
            ],
            height=320,
            margin=dict(t=10, b=10, r=10, l=10),
            showlegend=False,
        )
        
        st.plotly_chart(fig, use_container_width=True)
    s10, s20 = st.columns(2, vertical_alignment="center")

    with s20:
      if progress_value == 100:
        filled_part = (progress_value / 100) * 250
        empty_part = 250 - filled_part
        hidden_bottom = 110
        fig = go.Figure(
            data=[
                go.Pie(
                    values=[filled_part, empty_part, hidden_bottom],
                    rotation=237, 
                    direction="clockwise",
                    hole=0.8,
                    marker=dict(
                        colors=["#FF4B4B", "#E5E5E5", "rgba(0,0,0,0)"]
                    ),
                    hoverinfo="skip",
                    textinfo="none",
                    sort=False,
                )
            ]
        )
        
        fig.update_layout(
            annotations=[
                dict(
                    text=f"{progress_value}%",
                    x=0.5,
                    y=0.5,
                    font_size=42,
                    font_weight="bold",
                    showarrow=False,
                ),
                dict(
                    text="Diagnostic Progress",
                    x=0.5,
                    y=0.3,
                    font_size=14,
                    font_color="gray",
                    showarrow=False,
                )
            ],
            height=320,
            margin=dict(t=10, b=10, r=10, l=10),
            showlegend=False,
        )
        
        st.plotly_chart(fig, use_container_width=True)


# sidebar:
if st.user.is_logged_in:
  s1, s2 = st.sidebar.columns(2, vertical_alignment="center")
  with s1:
    try:
        with open(f"{st.user.email}strk.txt", "r") as f:
            v = f.read()
    except FileNotFoundError:
        with open(f"{st.user.email}strk.txt", "w") as f:
            f.write("n")
            v = "n"
    try:
        with open(f"{st.user.email}streak.txt", "r") as f:
            u = f.read()
    except FileNotFoundError:
        with open(f"{st.user.email}streak.txt", "w") as f:
            f.write("0")
            u = "0"
    if v == "y":
      with open(f"{st.user.email}streak.txt", "r+") as f:
          z = f.read()
      st.markdown(":color[:material/mode_heat:" + z + "]{foreground='#fa3002'}")
    elif v == "n" and u != "0":
        try:
            with open(f"{st.user.email}streak.txt", "r") as f:
                z = f.read()
        except FileNotFoundError:
            with open(f"{st.user.email}streak.txt", "w") as f:
                z = 0
        st.markdown(":color[:material/mode_heat: " + z + "]{foreground='#f0ab18'}")
    elif u == "0":
        st.markdown(":color[:material/mode_heat: 0]{foreground='#827f6c'}")
  with s2:
    @st.dialog("Test Score", dismissible=True)
    def show_popup_message(message_text):
        st.write(message_text)
    with open(f"{st.user.email}score.txt", "r+") as f:
        w = f.read()
    if st.button(f"{w}", type="tertiary", use_container_width=True):
        show_popup_message("The test score is used to define your overall improvements. The more positive feedback you receive, the higher your score goes, and the more negative feedback you receive, the lower your score goes. Your streak also affects your test score. If your streak is higher, your score will increase faster, while reducing the amount you decrease when given negative feedback. Complete a test every day (including diagnostics) to increase your streak. If you forget to test for just one day, your streak restarts at 0.")

with st.sidebar:
    if st.button("Log Out", icon=":material/logout:", use_container_width=True):
        st.session_state.guest_mode = False
        st.session_state.guest_login_time = None
        
        if st.user.is_logged_in:
            st.logout()
        else:
            st.rerun()

