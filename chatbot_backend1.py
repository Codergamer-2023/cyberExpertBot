from groq import Groq
from flask import Flask, request, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow frontend from port 5500 (VS Code Live Server or browser)
CORS(app,)

# Initialize Groq client
client = Groq(
    api_key="Your_API_Key",
)

@app.route('/', methods=['POST'])
def home():
    # Get the JSON data from the request
    data = request.get_json()
    user_input = data.get("message")

    # Validate input
    if not user_input:
        return jsonify({"error": "Missing 'message' field in request body."}), 400

    # Send chat history and current message to Groq API
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_completion_tokens=1024,
        stream=True,
        messages=user_input  # Full list of message dicts (system + previous chats + user)
    )

    # Yield response stream from the model
    def generate():
        for chunks in chat_completion:
            if chunks.choices[0].delta.content:
                yield chunks.choices[0].delta.content

    return Response(generate(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, port=5002)

