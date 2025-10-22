from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/check")
def check_number():
    number = request.args.get("number")
    if not number:
        return jsonify({"error": "missing number"}), 400

    # --- Simulated logic ---
    # You can replace this later with real logic (e.g. call your own DB or third-party source)
    status = random.choice(["Active", "Banned"])

    return jsonify({
        "number": number,
        "status": status,
        "message": f"{number} is {status} on WhatsApp🤖"
    })

@app.route("/")
def home():
    return "✅ DAX Ban-Checker API is alive but go use the api now 👀🥲"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
