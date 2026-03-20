from flask import Flask, jsonify,request
from model import get_question, check_answer
app = Flask(__name__)

@app.route('/question', methods=['GET'])
def question():
    return jsonify(get_question())

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    is_correct, feedback = check_answer(data['answer'])
    return jsonify({
        'is_correct': is_correct,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
