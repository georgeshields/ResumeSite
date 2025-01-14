import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai

# Ensure the OpenAI API key is set
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

app = Flask(__name__, static_folder='.', static_url_path='')  
CORS(app)
# Explanation:
#   static_folder='.'       tells Flask that our current directory is "static"
#   static_url_path=''      means serve files at "/"

@app.route("/", methods=["GET"])
def serve_html():
    # Serve the "chat.html" file when someone visits the root URL
    return send_from_directory('.', 'chat.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'reply': 'No message provided'}), 400

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        reply = response.choices[0].text.strip()
        return jsonify({'reply': reply})
    except Exception as e:
        return (jsonify({'reply': f'Error: {str(e)}'}), 500)

if __name__ == '__main__':
    app.run(debug=True)
