from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/owntracks', methods=['POST'])
def owntracks_webhook():
    data = request.get_json()  # Parse the JSON data sent by OwnTracks
    print("Received OwnTracks data:")
    print(data)

    # You can process the data further here if needed

    return jsonify({"message": "Data received successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app on a desired host and port
