import streamlit as st
import openai
from textblob import TextBlob
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env
openai_api_key = os.getenv("openai.api_key")
openai.api_key = openai_api_key

# Inject custom CSS for background and colors
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background-color: #f5f7fa;
    }
    .user-msg {
        background-color: #e3f2fd;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 5px;
        color: #1565c0;
        font-size: 16px;
    }
    .bot-msg {
        background-color: #fff3e0;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 5px;
        color: #ef6c00;
        font-size: 16px;
    }
    .sentiment-box {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
        color: #388e3c;
        font-size: 18px;
    }
    .coping-box {
        background-color: #fce4ec;
        border-radius: 10px;
        padding: 10px;
        margin-top: 10px;
        color: #ad1457;
        font-size: 18px;
    }
    .resources-box {
        background-color: #ede7f6;
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
        color: #4527a0;
        font-size: 16px;
    }
    .footer {
        background-color: #ffebee;
        border-radius: 10px;
        padding: 10px;
        margin-top: 30px;
        color: #c62828;
        font-size: 14px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Function to generate a response from GPT-3
def generate_response(prompt):
    try:
        # Get sentiment and coping strategy for context
        sentiment, polarity = analyze_sentiment(prompt)
        coping_strategy = provide_coping_strategy(sentiment)

        system_instruction = (
            "You are a compassionate and knowledgeable mental health support assistant. "
            "Your role is to provide empathetic, practical, and evidence-based advice to users who may be experiencing stress, anxiety, depression, or other mental health challenges. "
            "Always respond with kindness, encouragement, and actionable suggestions. "
            "If a user expresses severe distress or crisis, gently encourage them to seek professional help or contact emergency resources. "
            "Do not diagnose or prescribe medication. Maintain privacy and never ask for personal identifying information. "
            "Your responses should be detailed, supportive, and tailored to the user's emotional state."
        )

        user_message = (
            f"User message: {prompt}\n"
            f"Sentiment: {sentiment} (Polarity: {polarity})\n"
            f"Suggested coping strategy: {coping_strategy}\n"
            "Please provide a detailed, supportive response and suggest additional coping strategies or resources if appropriate."
        )

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.RateLimitError:
        pass


# Analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.5:
        return "Very Positive", polarity
    elif 0.1 < polarity <= 0.5:
        return "Positive", polarity
    elif -0.1 <= polarity <= 0.1:
        return "Neutral", polarity
    elif -0.5 < polarity < -0.1:
        return "Negative", polarity
    else:
        return "Very Negative", polarity


# Provide coping strategies (expanded detail)
def provide_coping_strategy(sentiment):
    strategies = {
        "Very Positive": (
            "😊 You're feeling very positive! Consider sharing your good mood with others, "
            "practicing gratitude, and engaging in activities that reinforce your happiness. "
            "Remember to savor these moments and reflect on what contributes to your positivity."
        ),
        "Positive": (
            "😃 It's great to see you're feeling positive. Keep doing what you're doing! "
            "You might benefit from setting new goals, helping someone else, or journaling about what's going well."
        ),
        "Neutral": (
            "😐 Feeling neutral is perfectly okay. You could try engaging in a favorite hobby, "
            "taking a walk, or practicing mindfulness to gently shift your mood if you wish."
        ),
        "Negative": (
            "😔 It seems you're feeling down. Try to take a break and do something relaxing, "
            "such as listening to music, talking to a friend, or practicing deep breathing exercises. "
            "Remember, it's okay to feel this way and reaching out for support can help."
        ),
        "Very Negative": (
            "😢 I'm sorry to hear that you're feeling very negative. Consider talking to a trusted friend, "
            "family member, or seeking professional help. You might also find comfort in grounding techniques, "
            "writing down your feelings, or engaging in gentle physical activity. If your distress feels overwhelming, "
            "please reach out to a mental health professional or helpline."
        )
    }
    return strategies.get(sentiment, "🌈 Keep going, you're doing great! Remember, support is always available.")


# App header with emoji
st.markdown("<h1 style='color:#1565c0;'>🧠 Mental Health Support Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#388e3c;font-size:18px;'>Welcome! This chatbot is here to support your mental health journey. 🌱</p>", unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'mood_tracker' not in st.session_state:
    st.session_state['mood_tracker'] = []

with st.form(key='chat_form'):
    user_message = st.text_input("Type your message here 💬")
    submit_button = st.form_submit_button(label='Send 🚀')

if submit_button and user_message:
    st.session_state['messages'].append(("You", user_message))

    sentiment, polarity = analyze_sentiment(user_message)
    coping_strategy = provide_coping_strategy(sentiment)

    response = generate_response(user_message)

    st.session_state['messages'].append(("Bot", response))
    st.session_state['mood_tracker'].append((user_message, sentiment, polarity))

# Display chat messages with colored containers and emojis
for sender, message in st.session_state['messages']:
    if sender == "You":
        st.markdown(f"<div class='user-msg'>🧑‍💻 <b>You:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>🤖 <b>Bot:</b> {message}</div>", unsafe_allow_html=True)

# Display sentiment and coping strategy in styled boxes
if st.session_state['mood_tracker']:
    last_message, last_sentiment, last_polarity = st.session_state['mood_tracker'][-1]
    st.markdown(f"<div class='sentiment-box'>📝 <b>Your current sentiment:</b> {last_sentiment}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='coping-box'>🛠️ <b>Suggested Coping Strategy:</b> {provide_coping_strategy(last_sentiment)}</div>", unsafe_allow_html=True)

# Display resources in main area
st.markdown("<div class='resources-box'><b>🌟 Resources</b><br>"
            "If you need immediate help, please contact one of the following resources:<br>"
            "1️⃣ National Suicide Prevention Lifeline: <b>1-800-273-8255</b><br>"
            "2️⃣ Crisis Text Line: Text '<b>HELLO</b>' to <b>741741</b><br>"
            "<a href='https://www.mentalhealth.gov/get-help/immediate-help' target='_blank'>More Resources</a>"
            "</div>", unsafe_allow_html=True)

# Display session summary in main area
if st.button("Show Session Summary 📋"):
    st.markdown("<h3 style='color:#4527a0;'>Session Summary</h3>", unsafe_allow_html=True)
    for i, (message, sentiment, polarity) in enumerate(st.session_state['mood_tracker']):
        st.markdown(f"<div class='sentiment-box'>{i + 1}. <b>{message}</b> <br>Sentiment: <b>{sentiment}</b></div>", unsafe_allow_html=True)

# Footer privacy disclaimer
st.markdown(
    "<div class='footer'>🔒 <b>Data Privacy Disclaimer</b><br>"
    "This application stores your session data, including your messages and sentiment analysis results, in temporary storage during your session. "
    "This data is not stored permanently and is used solely to improve your interaction with the chatbot. "
    "Please avoid sharing personal or sensitive information during your conversation.</div>",
    unsafe_allow_html=True
)