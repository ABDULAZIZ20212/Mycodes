import os
from json import JSONDecodeError
from flask import Flask, request, json, jsonify
import sentiment

api = Flask(__name__)

@api.route('/sentiment', methods=['POST'])
def post_snetiment():
    try:
        data = json.loads(request.data)
    except JSONDecodeError:
        return "Bad request", 400
    if data['text']:
        return jsonify(sentiment.analyze(data['text']))
    else:
        return "Error: Your request is missing a JSON body with text field", 400


if __name__ == '__main__':
    api.run(host='127.0.0.1', port= os.environ.get('PORT') or 8080)
