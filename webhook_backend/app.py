from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for received webhooks
webhooks = []

# Endpoint to receive webhooks
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    webhooks.append(data)
    print(f"Received webhook: {data}")
    return jsonify({"status": "success", "message": "Webhook received"}), 200

# Endpoint to get all webhooks (for frontend)
@app.route('/webhooks', methods=['GET'])
def get_webhooks():
    return jsonify(webhooks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

