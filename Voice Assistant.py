import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import openai

# Set your OpenAI API key (ensure your environment is secure)
openai.api_key = "YOUR_OPENAI_sk-proj-9Ib1aVOF2d5nxaRSGT6uT80RxvOM-5i_YroxhLLLnxPC4o358U6f9YG8gC9Qz_b710Ssamo_fqT3BlbkFJXYFAnm1XOV3UKXEN7WASNlrFWBQm2a8J-YgO4chPEvWjvfNwKtiknZ6lLy-8RtHeQc2WgHczIAAPI_KEY"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the speech service is down.")
        return ""

def tell_time():
    """Tell the current time."""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak("The time is " + now)

def tell_date():
    """Tell today's date."""
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak("Today is " + today)

def search_web(query):
    """Search the web using Google."""
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    speak("Searching the web for " + query)
    webbrowser.open(url)

def openai_response(query):
    """Generate a response using OpenAI's API for general queries."""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response["choices"][0]["text"].strip()
    return answer

def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        query = listen()
        if not query:
            continue

        if "hello" in query:
            speak("Hello! How can I assist you today?")
        elif "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "search" in query:
            # Remove the keyword "search" and use the rest as a query
            search_term = query.replace("search", "").strip()
            if search_term:
                search_web(search_term)
            else:
                speak("What would you like me to search for?")
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        else:
            # For other queries, use OpenAI to generate a response
            answer = openai_response(query)
            speak(answer)

if __name__ == "__main__":
    main()
