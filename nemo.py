
def AI():
    
    import os
    import time
    from openai import OpenAI
    import speech_recognition as sr
    import pyttsx3

    # Engine setup
    engine = pyttsx3.init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty('rate', 190)  # Increased speed

    # Ensure the 'Remember' directory exists
    file_path = "Remember/nemo.txt"
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

    # Query cleaning function
    def clean_query(query):
        stopwords = ["nemo", "jarvis", "ask ai", "nemotron"]
        for word in stopwords:
            query = query.replace(word, "").strip()
        return query

    # AI response function with proper file handling and timestamps
    def askNemo(query):
        try:
            client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key="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"
            )

            completion = client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[{"role": "user", "content": query}],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                stream=False
            )

            response = completion.choices[0].message.content
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get timestamp
            
            # Append response safely with timestamp
            with open(file_path, "a", encoding="utf-8") as ans:
                ans.write(f"\n[{timestamp}] {query}?\n{response}\n")

            print(response)
            speak(response)

        except Exception as e:
            print(f"Error: {e}")
            speak("There was an error processing your request.")
            


    def DelDataInnemotxt():
        if os.path.exists(file_path):
            with open(file_path, "w") as file:  # Opening in 'w' mode clears the file
                file.write("")  # Write an empty string to erase contents
            print(f"File '{file_path}' has been cleared.")
            speak("The previous data has been deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
            speak("The file doesn't exist, so there's nothing to delete.")

    # Main execution loop in AI
    speak("You are in Nemotron AI mode sir, You can ask anything!")

    while True:
        query = takeCommand().lower()

        if query == "none":
            continue

        elif "nemo" in query:
            prompt = clean_query(query)
            askNemo(prompt)
            
        
        elif any(phrase in query for phrase in ["thank you", "thanks"]):
            speak("You are welcome sir, I am always here to help you.")
        
        elif any(phrase in query for phrase in ["delete","clear","flush"]):
            DelDataInnemotxt()

        elif any(phrase in query for phrase in ["exit ai", "exit", "stop"]):
            speak("Thank you for using Nemotron AI sir, Have a nice day!")
            break

        else:
            speak("I am sorry, sir. I didn't understand that. Please try again.")



