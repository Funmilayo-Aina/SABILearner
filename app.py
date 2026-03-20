from flask import Flask, jsonify,request
from model import generate_question, check_answer,history

app = Flask(__name__)

@app.route('/question', methods=['GET'])
def question():
    return jsonify(generate_question())

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    result = check_answer(data["answer"])
    return jsonify(result)

@app.route("/progress", methods=["GET"])
def progress():
    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True)