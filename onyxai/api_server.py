from flask import Flask, request, jsonify
from onyxai.core import Core

app = Flask(__name__)
core = Core()

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    processed_data = core.ai_engine.process_data(data)
    return jsonify({"processed_data": processed_data})

@app.route("/transaction/<txn_id>", methods=["GET"])
def get_transaction(txn_id):
    status = core.blockchain_connector.get_transaction_status(txn_id)
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True)
