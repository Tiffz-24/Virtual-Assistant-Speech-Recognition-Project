import speech_recognition as sr #speech recognition library
import pyttsx3 #text to speech library
import datetime
from subprocesses import search_google, open_slack, youtube, open_word, open_camera, open_discord, open_notepad, open_facebook, send_email


def say_and_transcribe(engine, file, text):
    engine.say(text)
    engine.runAndWait()
    file.write(text)
    file.write('\n')

def get_datetime(engine, file):
    today = 'Today is: ' + str(datetime.date.today())
    say_and_transcribe(engine, file, today)
    time = 'The time is: ' + str(datetime.date.time())
    say_and_transcribe(engine, file, time)
def main():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', 1.0)
    engine.runAndWait()
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        # print('Clearing background noises..Please wait')
        # recognizer.adjust_for_ambient_noise(source, duration=1)
        file = open("audio-transcript.html", "wb")
        say_and_transcribe(file, 'Ask me anything...')
        print('Done!')
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio) #turn speech into text
            print("You said: ", command)
            say_and_transcribe(file, command)

            if 'stop' or 'exit' in command:
                say_and_transcribe(file, 'stopping now...')

            if 'date' or 'time' in command:
                get_datetime(engine, file) #function returns current date and time

            if 'open camera' in command:
                open_camera(engine)

            if 'google search' or 'search google' in command:
                say_and_transcribe(file, 'What would you like to search?')
                say_and_transcribe(file, 'Searching Google...')
                search_google(engine)

            if 'open youtube' or 'search youtube' in command:
                say_and_transcribe(file, 'What video you like to play?')
                say_and_transcribe(file, 'Opening youtube...')
                youtube(engine)

            if 'open slack' in command:
                say_and_transcribe(file, 'Opening slack...')
                open_slack(engine)

            if 'open discord' in command:
                say_and_transcribe(file, 'Opening discord..')
                open_discord(engine)

            if 'open word' or 'open microsoft word' in command:
                say_and_transcribe(file, 'Opening word...')
                open_word(engine)

            if 'open notepad' in command:
                say_and_transcribe(file, 'Opening notepad...')
                open_notepad(engine)

            if 'open facebook' in command:
                say_and_transcribe(file, 'Opening facebook...')
                open_facebook(engine)

            if 'send email' in command:
                say_and_transcribe(file, "What email address would you like to send an email to?")
                receiver = input("Enter email address here: ")
                say_and_transcribe(file, "What should the subject line be")
                subject = input("Enter subject line here: ")
                say_and_transcribe(file, "What shall the message be?")
                message = input("Enter message here: ")
                say_and_transcribe(file, 'Sending email....')
                send_email(engine, receiver, subject, message)

            #if detect sass, fire back with a roast
        except:
            say_and_transcribe(file, 'Could not recognize audio. Try again')

while 1:
    if __name__ == '__main__':
        main()