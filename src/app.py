from flask import Flask, jsonify, request,send_file

app = Flask(__name__)

@app.route('/login/')
def incrementer():
    return "Login Page"

@app.route('/CityModule')
def hello():
    return "Hello "

@app.route('/home/')
def home():
    return "Home Page"

@app.route('/contact')
def contact():
    return "Contact"

if __name__ == '__main__':
    app.run(debug=True, port=4890)