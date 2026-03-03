import streamlit as st
import time

st.set_page_config(page_title="Birthday Surprise Bae 💖", layout="centered")

st.title("🎉 A Special Surprise Bae 🎁")

name = st.text_input("From Atharvi💕")

if st.button("Open Your Surprise 💝"):
    st.balloons()
    time.sleep(1)

    st.markdown(f"## 🎂 Happy Birthday Kasturi 💖")
    st.markdown("### You are the most precious person in my life 💕")

    st.write("""
    I am so lucky to have you.
    Thank you for your love, your care, your support,
    and for making my life brighter every single day.
    """)

    st.markdown("## 📸 Our Beautiful Memories")

    col1, col2 = st.columns(2)

with col1:
    st.image("photo1.jpeg", caption="My sunshine ☀️")

with col2:
    st.image("photo2.jpeg", caption="My happiness 💕")

st.image("photo3.jpeg", caption="Forever us ❤️")

st.markdown("---")
st.markdown("💌 Made with love, just for you Bae.")
