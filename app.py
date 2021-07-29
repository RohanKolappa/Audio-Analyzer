from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"]) #the '/' tells us that we are routing to the home page
#GET requests are for receiving data
#POST requests are for taking data from a user input and sending it to another destination


def index():
    if request.method == "POST":
        print("FORM DATA RECEIVED")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True, threaded = True)
    """debug will allow us to automatically save the file, and the Flask instance will 
    have the latest updates. In other words, any changes I make to the file will automatically 
    be sent to the Flask instance once I refresh"""
    """threaded will allow us to process multiple requests at the same time"""

