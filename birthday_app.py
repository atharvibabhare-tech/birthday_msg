import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title=" Birthday Surprise Bae 💖", layout="centered")

st.title("🎉 A Special Surprise For You Bae 🎁")

name = st.text_input("From Atharvi💕")

# 🎵 MUSIC BUTTON
st.markdown("### 🎶 Click below to play our song")
st.audio("perfect.mp3")

def slow_text(text):
    placeholder = st.empty()
    full_text = "💋"
    for char in text:
        full_text += char
        placeholder.markdown(full_text)
        time.sleep(0.03)

if st.button("Open Your Surprise Bae 💝"):

    st.balloons()
    st.snow()
    time.sleep(2)

    st.markdown("## 🎂 Happy Birthday Kasturi 💖")
    st.markdown("### You are the most precious person in my life 💕")

    slow_text("I am so lucky to have you.")
    time.sleep(0.5)
    slow_text("Thank you for your love, your care, your support.")
    time.sleep(0.5)
    slow_text("You make my life brighter every single day.")
    time.sleep(0.5)
    slow_text("I love you more than words can ever explain ❤️")

    st.markdown("## 💞 Our Journey of Friendship ")

    start_date = datetime(2023, 11, 20)
    today = datetime.now()
    days_together = (today - start_date).days

    st.success("We have been together for 3 beautiful years and one thing will never change — our SUPPORT for each other 💕")

    st.markdown("## 📸 Our Beautiful Memories")

    col1, col2 = st.columns(2)

    with col1:
        st.image("photo1.jpeg", caption="My sunshine ☀️")

    with col2:
        st.image("photo2.jpeg", caption="My happiness 💕")

    st.image("photo3.jpeg", caption="Forever us ❤️")

    st.markdown("---")

# session states
if "show_love" not in st.session_state:
    st.session_state.show_love = False

if "show_forever" not in st.session_state:
    st.session_state.show_forever = False


if st.button("Why I Love You? Everytime You Ask Me 💖"):
    st.session_state.show_love = True

if st.session_state.show_love:
    st.write("""
💕 Your smile  
💕 Your eyes  
💕 Your Hugs 
💕 The way you kiss my forehead  
💕 The way you understand me  
💕 I can LEAVE U but still come back to u...!!!
""")


st.markdown("---")

if st.button("Will you stay with me forever?"):
    st.session_state.show_forever = True

if st.session_state.show_forever:
    st.balloons()
    st.success("I promise to always choose you bae , in future we may be not as a GF but as a Bestfriend Always ❤️")
