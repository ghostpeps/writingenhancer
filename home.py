import streamlit as st
from datetime import datetime, timedelta, timezone
import pytz
import plotly.graph_objects as go

col1, col2 = st.columns(2)

user_tz_str = st.context.timezone

if user_tz_str:
    tz_obj = pytz.timezone(user_tz_str)
    local_time = datetime.now(timezone.utc).astimezone(tz_obj)
    formatted_time = local_time.strftime("%H:%M:%S.%f")
    if formatted_time == "00:00:00.000000":
        try:
            with open(f"{st.user.email}strk.txt", "r") as f:
                pass
        except FileNotFoundError:
            with open(f"{st.user.email}strk.txt", "w") as f:
                pass
        try:
            with open(f"{st.user.email}streak.txt", "r") as f:
                pass
        except FileNotFoundError:
            with open(f"{st.user.email}streak.txt", "w") as r:
                r.write("0")
        with open(f"{st.user.email}strk.txt", "r+") as f:
            if f.read() == "n":
                with open(f"{st.user.email}streak.txt", "r+") as r:
                    r.write("0")
            elif f.read() == "y":
                f.write("n")
if st.user.is_logged_in:
    try:
        with open(f"{st.user.email}d.txt", "r") as f:
            progress_value = int(f.read())
    except FileNotFoundError:
        with open(f"{st.user.email}d.txt", "w") as f:
            f.write("0")
            progress_value = 0
    
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

with col1:
    st.title("Home")
    
    if st.user.is_logged_in:
        st.write(f"Welcome, {st.user.name}")
        st.write(f"Email: {st.user.email}")
        st.write(f"Preferred Language: {st.context.locale}")
    else:
        st.write("Logged in without an account")

with col2:
    st.title("Tests")
    if st.user.is_logged_in:
        try:
            with open(f"{st.user.email}grade.txt", "r", encoding="utf-8") as f:
                if "G" == f.read(1):
                    y = True
        except FileNotFoundError:
            y = False
        if not y:
            grade = st.selectbox("Please choose your grade to start testing", ("1", "2", "3", "4", "5", "6"), None)
            if grade:
                with open(f"{st.user.email}grade.txt", "a", encoding="utf-8") as f:
                    f.write(f"Grade {grade}")
        elif y:
            grade = st.selectbox("Change Grade", ("1", "2", "3", "4", "5", "6"), None)
            if grade:
                with open(f"{st.user.email}grade.txt", "rb+") as f:
                    f.seek(6, 0)
                    x = f"{grade}"
                    f.write(x.encode("utf-8"))
            st.write("Tests will be here")
            with open(f"{st.user.email}grade.txt", "r", encoding="utf-8") as f:
                st.write(f.read())
    else:
        if st.session_state.selected_grade not in (1, 2, 3, 4, 5, 6):
            grade = st.selectbox("Please choose your grade to start testing", ("1", "2", "3", "4", "5", "6"), None)
            if grade:
                st.session_state.selected_grade = int(grade)
                st.rerun()
        elif st.session_state.selected_grade in (1, 2, 3, 4, 5, 6):
            grade = st.selectbox("Change Grade", ("1", "2", "3", "4", "5", "6"), None)
            if grade:
                st.session_state.selected_grade = int(grade)
            st.write("Grade " + str(st.session_state.selected_grade))
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
            try:
                with open(f"{st.user.email}streak.txt", "r") as f:
                    z = int(f.read()) + 1
            except FileNotFoundError:
                with open(f"{st.user.email}streak.txt", "w") as f:
                    z = 0
            with open(f"{st.user.email}streak.txt", "w") as f:
                f.write(f"{z}")
            st.markdown(":color[:material/mode_heat: " + str(z) + "]{foreground='#fa3002'}")
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
        try:
            with open(f"{st.user.email}score.txt", "r") as f:
                w = int(f.read())
        except FileNotFoundError:
            with open(f"{st.user.email}score.txt", "w") as f:
                f.write("0")
                w = 0
        if st.button(f"{w}", type="tertiary", use_container_width=True):
            show_popup_message("The test score is used to define your overall improvements. The more positive feedback you receive, the higher your score goes, and the more negative feedback you receive, the lower your score goes. Your streak also affects your test score. If your streak is higher, your score will increase faster, while reducing the amount you decrease when given negative feedback. Complete a test every day (including diagnostics) to increase your streak. If you forget to test for just one day, your streak restarts at 0.")
with st.sidebar:
    if st.session_state.get("guest_mode") and st.session_state.get("guest_login_time"):
        start_time = st.session_state.guest_login_time
        expiration_time = start_time + timedelta(hours=24)
        current_time = datetime.now()
        time_left = expiration_time - current_time
        total_seconds = int(time_left.total_seconds())
        
        if total_seconds > 0:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            st.metric(label="Time until automatically logged out:", value=f"{hours}:{minutes}")
        else:
            st.error("Session expired! Refreshing...")
        
    if st.button("Log Out", icon=":material/logout:", use_container_width=True):
        st.session_state.guest_mode = False
        st.session_state.guest_login_time = None
        if st.user.is_logged_in:
            st.logout()
        else:
            st.rerun()

