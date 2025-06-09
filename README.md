# 🤖 Jarvis - AI Desktop Voice Assistant
# J.A.R.V.I.S. – Just A Rather Very Intelligent System
# Just Another Robotic Voice-Integrated System
**Jarvis** is an intelligent, modular, and powerful desktop voice assistant written in Python. It responds to voice commands, automates your tasks, integrates online services, and delivers a smart AI assistant experience — directly from your terminal.

> Think of it as your own custom-built J.A.R.V.I.S from Iron Man 🦾

---

## 🧠 Core Features

- 🔐 **Password-Protected Access** (3 chances to log in)
- 🎙️ **Voice-Activated**: Say “**wake up**” to activate
- 📅 **Task Scheduling & Notifications**
- 🌐 **Voice-Based Web Search**:
  - Google, YouTube, Wikipedia, Perplexity
- 🎬 **IMDb Movie Info Lookup**
- 📩 **Send Emails Using Your Voice**
- 💬 **WhatsApp Automation**
- 🎧 **Spotify Music Integration**
- ⏰ **Alarms & Reminders**
- 📡 **Internet Speed Testing**
- 📸 **Take Screenshots and Webcam Photos**
- 🌦️ **Weather Forecast and Temperature Info**
- 🧠 **Memory Function**: “Remember that...”
- 📊 **Focus Mode with Productivity Tracking**
- 🧠 **AI Tools Integration**: Gemini & Nemo
- 🎮 **Game Launcher**
- 🖥️ **Open/Close Desktop Apps/Websites**
- 🧾 **Real-Time News Reader**
- 🌍 **IP Address & Location Detection**
- 🔁 **Translator (Multi-language Support)**
- 🔊 **YouTube Media Control (Play, Pause, Mute, Volume)**
- 📜 **General Knowledge & Math via WolframAlpha**

---

## 🚀 How to Get Started

### ✅ Prerequisites

Ensure Python 3.8+ is installed.

Install the dependencies:

```bash
pip install pyttsx3 SpeechRecognition requests beautifulsoup4 pygame plyer pyautogui speedtest-cli keyboard

📁 Folder Structure

Jarvis/
├── jarvis_main.py               # Main assistant file
├── alarm.py                     # Alarm script
├── FocusMode.py                 # Focus mode module
├── FocusGraph.py                # Productivity graph
├── omnitrix.mp3                 # Notification sound
├── Passwordfile/password.txt    # Stores login password
├── Tasks/tasks.txt              # Saved daily tasks
├── Remember/rememberMe.txt      # Stores memory prompts
├── Modules/
│   ├── weather_forecast.py
│   ├── SearchNow.py
│   ├── GamesSearch.py
│   ├── NewsRead.py
│   ├── calculateNum.py
│   ├── Whatsapp.py
│   ├── SendEmail.py
│   ├── online.py
│   ├── Dictapp.py
│   ├── spotify.py
│   ├── Translator.py
│   ├── subscribe.py
│   ├── Imdb.py
│   └── GreetMe.py
Make sure the directories Passwordfile/, Tasks/, and Remember/ exist with writable .txt files.

▶️ How to Run
python jarvis_main.py

1.Enter your password (stored in Passwordfile/password.txt)

2.Say “wake up” to activate the assistant

3.Start giving voice commands!


🗣️ Example Commands
•General:

    “What’s the temperature?”

    “Send an email”

    “Take a screenshot”

    “Play music”

    “Schedule my day”

•App & Web Control:

    “Open calculator”

    “Close browser”

    “Search YouTube for lo-fi music”

•Productivity & Focus:

    “Focus mode”

    “Show my focus”

    “Remember that I have a meeting at 5 PM”

•Fun & AI Tools:

    “Start a game”

    “Translate hello to Spanish”

    “Use Gemini”

    “Use Nemo”


✨ Customization
•🎨 Personalize Responses: Edit text in speak() to customize Jarvis’ tone

•🔊 Change Voice/Rate: Modify pyttsx3 config in jarvis_main.py

•🎶 Update Music Links: In “tired” mode section, add your favorite YouTube links

•🧩 Add New Features: Extend modular functions in external .py files

⚠️ Notes
•Works best on Windows (due to sapi5 voice engine)

•Some modules (e.g., email, WhatsApp) may require additional setup like SMTP auth or web login

•All features are offline-capable, except those that rely on online APIs (search, email, weather, etc.)

🧑‍💻 Author
Eswarpavanteja Dhavala

Built with passion for automation, voice interfaces, and productivity.

📜 License
This project is intended for personal and educational use. Modify and extend it at your own discretion.

💡 Future Ideas (Optional Enhancements)
•GUI with PyQt or Tkinter

•Integration with ChatGPT API

•Calendar sync with Google Calendar

•Voice-activated file search or file manager

•Offline NLP engine for fallback

Thank you for checking out Jarvis — your AI-powered desktop assistant!
🗣️ “Wake up, Jarvis!” and get to work! 🦾


