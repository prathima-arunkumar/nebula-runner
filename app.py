from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/operation/verify', methods=['GET'])
def verify():
    return jsonify(status="Running smoothly")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
