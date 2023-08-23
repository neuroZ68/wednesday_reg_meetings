from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    return jsonify({'list': ['pig1', 'pig2', 'pig3']})

if __name__ == '__main__':
    app.run(debug=True)