from flask import Flask, render_template, request, redirect
import speech_recognition as sr



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"]) #the '/' tells us that we are routing to the home page
#GET requests are for receiving data
#POST requests are for taking data from a user input and sending it to another destination


def index():
    if request.method == "POST":
        print("FORM DATA RECEIVED")

    if "file" not in request.files: #failsafe in case file does not exist
        return redirect(request.url)

    file = request.files["file"]
    if file.filename == "": #failsafe in case file is blank
        return redirect(request.url)

    if file: #file exists
        r = sr.Recognizer() #initializing the instance of the speech recognition class
        audioFile = sr.AudioFile(file) #AudioFile object is created (that the SR module can interpret)
        with sr.audioFile as source: #opening and reading the file that we created through the recognizer
            audio = r.record(source)
            text = r.recognize_google(audio, key=None) #Google Cloud Speech API will be used to convert the audio into text
            print(text)


        try:
            print("Transcription: " + r.recognize(audio))
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True, threaded = True)
    """debug will allow us to automatically save the file, and the Flask instance will 
    have the latest updates. In other words, any changes I make to the file will automatically 
    be sent to the Flask instance once I refresh"""
    """threaded will allow us to process multiple requests at the same time"""

