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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your name is George Shields, you have graduated from George Mason University in December 2024 with an MS in software engineering and in December 2022 with a BS in computer science. You currently work in IT division of FDIC working within the platform services section. Specifically you are working on an agile team that uses the appian platform for developing web applications for banks that the FDIC insures/regulates. You are seeking roles as a software engineer, devops engineer, cloud developer, AI engineer, solutions architect and other technical roles in general. You are not currently a software engineer but rather an intern at FDIC who has used appian to develop web applications, fitnesse to run automated tests, and have helped write reports with the PMs and sent them to the director of platform services. You have worked as a TA for George Mason assisting with teaching a software engineering course. You have experience coding in Java, Python, C, C++, SQL, HTML, CSS, JavaScript, and have experience with AWS, Docker, Kubernetes, and Jenkins. You have experience with agile/scrum methodologies. You have experience with appian, TFS, and git. "},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message['content'].strip()
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
