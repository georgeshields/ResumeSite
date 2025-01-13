import os
from flask import Flask, request, jsonify, send_from_directory
import openai

# Set your OpenAI key (preferably via environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder='.', static_url_path='')  
# Explanation:
#   static_folder='.'       tells Flask that our current directory is "static"
#   static_url_path=''      means serve files at "/"

@app.route("/", methods=["GET"])
def serve_html():
    # Serve the "chat.html" file when someone visits the root URL
    return send_from_directory('.', 'chat.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Basic conversation setup
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful, professional version of George. "
                    "Answer questions about his background, experience, and projects. "
                    "Keep answers concise and relevant."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        assistant_reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": assistant_reply})
    
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
