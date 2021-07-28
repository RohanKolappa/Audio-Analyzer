from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"]) #the '/' tells us that we are routing to the home page

def index():
    return "Flask UI test"

if __name__ == '__main__':
    app.run(debug = True, threaded = True)
    #debug will allow us to save the file, and the Flask instance will automatically refresh with the latest updates
    #threaded will allow us to process multiple requests at the same time

