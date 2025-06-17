from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Virtual TA API is live! Use POST /api/ with a question.", 200

@app.route("/api/", methods=["POST"])
def virtual_ta():
    data = request.get_json()
    question = data.get("question", "")
    
    return jsonify({
        "answer": f"You asked: {question}. This is a sample response.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/",
                "text": "Sample link to Discourse"
            }
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
