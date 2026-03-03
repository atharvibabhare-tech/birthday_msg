import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Birthday Surprise Bae 💖", layout="centered")

st.title("🎉 A Special Surprise For You Bae 🎁")

name = st.text_input("From Atharvi💕")

# 🎵 Background Music 
st.markdown("""
<iframe width="0" height="0"
src="https://www.youtube.com/embed/2Vv-BfVoq4g?autoplay=1"
frameborder="0" allow="autoplay"></iframe>
""", unsafe_allow_html=True)

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
    time.sleep(1)

    st.markdown(f"## 🎂 Happy Birthday Kasturi 💖")
    st.markdown("### You are the most precious person in my life 💕")

    slow_text("I am so lucky to have you.")
    time.sleep(0.5)
    slow_text("Thank you for your love, your care, your support.")
    time.sleep(0.5)
    slow_text("You make my life brighter every single day.")
    time.sleep(0.5)
    slow_text("I love you more than words can ever explain ❤️")

    st.markdown("## 💞 Our Journey of Friendship ")

    start_date = datetime(2023, 11, 20)  # CHANGE THIS TO YOUR REAL DATE
    today = datetime.now()
    days_together = (today - start_date).days

    st.success(f"We have been together for 3 beautiful years together and in those 3yrs too many things get change between us but one thing is common that will never change is SUPPORT for each other 💕")

    st.markdown("## 📸 Our Beautiful Memories")

    col1, col2 = st.columns(2)

    with col1:
        st.image("photo1.jpeg", caption="My sunshine ☀️")

    with col2:
        st.image("photo2.jpeg", caption="My happiness 💕")

    st.image("photo3.jpeg", caption="Forever us ❤️")

    st.markdown("---")

    if st.button("Why I Love You u everytime ask me 💖"):
        st.write("""
        💕 Your smile  
        💕 Your eyes  
        💕 Your strength  
        💕 The way you kiss on my forehead and hold my hands
        💕 The way you understand me sometimes hehe
        💕 Everything about you. How can I forget this all happy and peacefull moments with you bae?
        """)

    st.markdown("---")

    if st.button("Will you stay with me forever? "):
        st.balloons()
        st.success("I promise to always choose you. Always Bae, dont be scared if not as a couple but as a bestfriend...❤️")
