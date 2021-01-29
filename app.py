from flask import Flask, make_response, jsonify, request, render_template
from flask_cors import CORS, cross_origin
from bot.chat import init_bot, chat

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
intents, all_words, tags, model, device = init_bot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
@cross_origin()
def get_bot_response():
    sentence = request.json['sentence']
    response = chat(sentence, intents, all_words, tags, model, device)
    return make_response(jsonify({"response" : response}), 200)
   

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(debug=True)