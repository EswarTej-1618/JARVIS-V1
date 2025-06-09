
def Gemini():
    
    import os
    import time
    import speech_recognition as sr
    import pyttsx3
    from google import genai

    # Replace with your actual API key from Google AI Studio
    api_key = "AIzaSyAhKs3XiXVvArL-lKtnf1bLP9kUDuGpgEI"
    client = genai.Client(api_key=api_key)

    # Engine setup
    engine = pyttsx3.init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty('rate', 190)  # Increased speed

    # Ensure the 'Remember' directory exists
    file_path = "Remember/gemini.txt"
    if not os.path.exists("Remember"):
        os.makedirs("Remember")

    # Text-to-speech function
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    # Voice command function
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1  # Reduced pause time for faster recognition
            r.energy_threshold = 300
            audio = r.listen(source)
            
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return query.lower()
        except Exception:
            print("Could you please say that again, sir!")
            return "None"

    # AI response function
    def askGemini(query):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=query
            )
            response_text = response.text
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get timestamp

            # Append response safely with timestamp
            with open(file_path, "a", encoding="utf-8") as ans:
                ans.write(f"\n[{timestamp}]{query}?\n{response_text}\n")

            print(response_text)
            speak(response_text)

        except Exception as e:
            print(f"Error: {e}")
            speak("There was an error processing your request.")

    # Function to clear stored data
    def clearGeminiData():
        if os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("")  # Write an empty string to erase contents
            print(f"File '{file_path}' has been cleared.")
            speak("The previous data has been deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
            speak("The file doesn't exist, so there's nothing to delete.")

    # Main execution loop in AI
    speak("You are in Gemini AI mode sir, you can ask anything!")

    while True:
        query = takeCommand().lower()

        if query == "none":
            continue

        elif "gemini" in query:
            askGemini(query)

        elif any(phrase in query for phrase in ["thank you", "thanks"]):
            speak("You are welcome! I am always here to help you sir.")

        elif any(phrase in query for phrase in ["delete", "clear", "flush"]):
            clearGeminiData()

        elif any(phrase in query for phrase in ["exit ai", "exit", "stop"]):
            speak("Thank you for using Gemini AI. Have a great day! sir.")
            break

        else:
            speak("I am sorry, I didn't understand that. Please try again.")

