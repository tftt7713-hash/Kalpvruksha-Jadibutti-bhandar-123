import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mera Chatbot", layout="centered")
st.title("🤖 Mera AI Chatbot")

# Jo link aapne Chatbase se copy kiya hai, use yahan src ki jagah paste karein
chatbot_url = "https://www.chatbase.co/chatbot-iframe/Yo9IAwiCy3KAPOyzOWzHC"

# Yeh line chatbot ko screen par dikhayegi
components.iframe(chatbot_url, height=600, scrolling=True)
