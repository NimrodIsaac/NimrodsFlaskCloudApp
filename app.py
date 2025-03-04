from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Nimrod Maingi for President 2027!"

if __name__ == '__main__':
    app.run(debug=True)
