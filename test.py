import streamlit as st
import random
import time

# List of compliments
compliments = [
    "You light up every room you walk into ✨",
    "Spending time with you is my favorite thing ❤️",
    "You’re smarter and cuter than any code I could write 💻💕",
    "Every day with you feels special 🌸",
    "You're my favorite notification 🔔❤️",
    "One smile from you makes my whole day better 😊"
]

final_message = "💌 This app was made just for you... because you’re truly special to me 💕"

# Track button clicks with session_state
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

st.set_page_config(page_title="A Special Surprise 💌", page_icon="❤️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff3366;'>Hi, Beautiful 💖</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 80px;'>❤️</h2>", unsafe_allow_html=True)

if st.button("Click me 💕"):
    st.session_state.clicks += 1

if st.session_state.clicks > 0:
    if st.session_state.clicks < 5:
        st.success(random.choice(compliments))
    else:
        st.balloons()
        st.markdown(
            f"<h3 style='text-align: center; color: #660033;'>{final_message}</h3>",
            unsafe_allow_html=True
        )
