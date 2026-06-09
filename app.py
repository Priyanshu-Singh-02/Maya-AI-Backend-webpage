import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API Key Setup
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("CRITICAL ERROR: API Key nahi mili!")
else:
    genai.configure(api_key=api_key)

@app.route('/api/ask', methods=['POST'])
def ask():
    # Aapka AI logic yahan aayega
    return jsonify({"reply": "Maya is online and working!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
