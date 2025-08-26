
# 🧠 Mental Health Support Chatbot

This project is a Mental Health Support Chatbot built using [Streamlit](https://streamlit.io/) and [OpenAI's GPT-3.5-turbo model](https://platform.openai.com/docs/models/gpt-3-5-turbo). It provides mental health support through a chat interface, offering sentiment analysis, mood tracking, and personalized coping strategies based on user input.

A compassionate, evidence-based chatbot built with Streamlit and OpenAI to support users on their mental health journey. It analyzes user sentiment, suggests coping strategies, and provides helpful resources—all while maintaining privacy and empathy.


## ✨ Features
- 💬 **Conversational Support:** Chat with an AI assistant trained to provide empathetic, practical advice for stress, anxiety, depression, and more.
- 📊 **Sentiment Analysis:** Uses TextBlob to analyze your emotional state and tailors responses accordingly.
- 🛠️ **Coping Strategies:** Suggests actionable, evidence-based coping strategies based on your mood.
- 🔗 **Resource Links:** Offers immediate help resources and links to professional support.
- 📋 **Session Summary:** View a summary of your session's messages and mood changes.
- 🔒 **Privacy:** No personal data is stored permanently. All session data is temporary.


## ⚡ Setup Instructions


### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Mental-Health-Support-Chatbot.git
```


### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv env
env\Scripts\activate
```


### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```


### 4️⃣ Set Up OpenAI API Key
Create a `.env` file in the project root:
```
openai.api_key=YOUR_OPENAI_API_KEY
```


### 5️⃣ Run the App
```bash
streamlit run app.py
```


## 💡 Usage
- Type your message in the chat box and press "Send 🚀".
- View your sentiment and suggested coping strategies after each message.
- Access mental health resources and session summary as needed.


## ⚠️ Important Notes
- 🚫 **Do not share personal or sensitive information.**
- 💊 **This app does not diagnose or prescribe medication.**
- 🆘 **For emergencies, contact professional help or use the provided resources.**


## 📦 Dependencies
- streamlit
- openai
- textblob
- pandas
- python-dotenv


## 📄 License
This project is licensed under the MIT License.


## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


## 🙏 Acknowledgements
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [MentalHealth.gov](https://www.mentalhealth.gov/)


---

*🤖 This chatbot is for informational and supportive purposes only. For professional help, please consult a licensed mental health provider.*

