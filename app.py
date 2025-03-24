from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Flask App</h1>"

if __name__ == "_main_":
    app.run()