import streamlit as st
import time

st.set_page_config(page_title="Birthday Surprise Bae 💖", layout="centered")

st.title("🎉 A Special Surprise 🎁")

name = st.text_input(" Atharvi 💕")

if st.button("Open Your Surprise 💝"):
    st.balloons()
    time.sleep(1)

    st.markdown(f"## 🎂 Happy Birthday {Kasturi} 💖")
    st.markdown("### You are the most precious person in my life 💕")

    st.write("""
    I am so lucky to have you.
    Thank you for your love, your care, your support,
    and for making my life so much brighter.
    
    I promise to always stand beside you,
    celebrate your wins,
    support your dreams,
    and love you endlessly. ❤️
    """)

    st.markdown("### 🎁 Today is all about YOU!")
    st.markdown("Keep shining. Keep smiling. Keep being amazing. ✨")

    st.markdown("---")
    st.markdown("💌 Made with love just for you bae.")
