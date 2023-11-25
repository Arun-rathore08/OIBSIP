
import random
from urllib import request
import speech_recognition as sr
import pyttsx3
import openai
from newsapi import NewsApiClient
import wikipediaapi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up your API keys and email credentials
openai.api_key = "38b46d9d2255a70fcc8179e9a6466a33"
newsapi = NewsApiClient(api_key="767a05b59bac4db6b23de42235516317")
#user_agent = "https://whatismybrowser.com/w/3X2BFZW"
#wikipedia = wikipediaapi.Wikipedia('en')
user_agent = "https://whatismybrowser.com/w/3X2BFZW"
#wikipedia.set_user_agent(user_agent)


email_address = "08arunrathore@gmail.com"
email_password = " "
recipient_email = "recipient_email@gmail.com"

def greet():
    greetings = ["Hello!", "Hi!", "Greetings!"]
    return random.choice(greetings)

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Virtual Assistant: Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        print("You:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Virtual Assistant: Sorry, I didn't catch that. Can you repeat?")
        return get_voice_input()
    except sr.RequestError as e:
        print(f"Virtual Assistant: Could not request results from Google Speech Recognition service; {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_weather():
    # Replace with your city and OpenWeatherMap API key
    city = "YourCity"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openai.api_key}"
    response = openai.get(url).json()

    if response["cod"] != "404":
        weather_description = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        return f"The weather in {city} is {weather_description}. The temperature is {temperature} degrees Celsius."
    else:
        return "Sorry, I couldn't fetch the weather information."

def get_news():
    top_headlines = newsapi.get_top_headlines(language='en', country='us')
    articles = top_headlines['articles']

    if articles:
        news_text = "Here are the top headlines: "
        for article in articles:
            news_text += f"{article['title']}. "
        return news_text
    else:
        return "Sorry, I couldn't fetch the news."

def get_wikipedia_info(topic):
    wikipedia_api_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&titles={topic}&prop=extracts&exintro&explaintext"
    
    headers = {
        "User-Agent": user_agent,
    }

    try:
        response = request.get(wikipedia_api_url, headers=headers)
        data = response.json()
        page_id = list(data["query"]["pages"].keys())[0]
        summary = data["query"]["pages"][page_id]["extract"]
        return summary
    except Exception as e:
        # Handle exceptions as needed
        return f"Error: {e}"

def send_email(subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)

        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.send_message(msg)
        server.quit()
        return "Email sent successfully."
    except Exception as e:
        return f"Error sending email: {e}"

def process_command(command):
    if "how are you" in command:
        return "I'm doing well, thank you!"
    elif "your name" in command:
        return "I am your virtual assistant."
    elif "weather" in command:
        return get_weather()
    elif "news" in command:
        return get_news()
    elif "tell me about" in command:
        topic = command.split("tell me about", 1)[1].strip()
        return get_wikipedia_info(topic)
    elif "send email" in command:
        speak("What is the subject of the email?")
        subject = get_voice_input()
        speak("What should be the content of the email?")
        body = get_voice_input()
        return send_email(subject, body)
    elif "bye" in command or "exit" in command:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand that command."

def main():
    speak("Virtual Assistant: " + greet())

    while True:
        user_input = get_voice_input()
        if user_input is None:
            continue

        if user_input.lower() == 'exit':
            speak("Virtual Assistant: Goodbye!")
            break

        response = process_command(user_input)
        speak("Virtual Assistant: " + response)

if __name__ == "__main__":
    main()
