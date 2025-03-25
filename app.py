# from flask import Flask

# app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def home():
#     return "<h1>Flask App</h1>"

# if __name__ == "_main_":
#     app.run()




from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route to render the frontend
@app.route('/')
def index():
    return render_template('index.html')

# API to receive user data
@app.route('/user-details', methods=['POST'])
def get_user_details():
    user_data = request.json
    return jsonify({
        "message": "User details received successfully!",
        "user": user_data
    })

if __name__ == '__main__':
    app.run(debug=True)
