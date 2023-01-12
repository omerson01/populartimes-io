import populartimes
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/populartimes')
def hello():
    api_key = request.args.get('api_key')
    place_id = request.args.get('place_id')
    return jsonify(message=populartimes.get_id(api_key, place_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
