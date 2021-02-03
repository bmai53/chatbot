from flask import Flask, make_response, jsonify, request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from bot.chatbot import ChatBot
import json
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

bot = ChatBot()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
@cross_origin()
def get_bot_response():
    sentence = request.json['sentence']
    response = bot.chat(sentence)
    print(response)
    return make_response(jsonify(response), 200)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), 'favicon.ico')


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(debug=True)
