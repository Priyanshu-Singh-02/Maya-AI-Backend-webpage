from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
# CORS enable kiya taaki Netlify frontend is backend se secure baat kar sake
CORS(app, resources={r"/*": {"origins": "*"}})

# Maya ka System Prompt (Uski personality set karne ke liye)
MAYA_PERSONALITY = (
    "Your name is Maya. You are a brilliant, friendly, and highly premium female AI Assistant. "
    "You were created by Priyanshu Singh (Rudra). Always maintain a warm, polite, and respectful tone. "
    "Keep your answers engaging, short, and clean so that they can be easily spoken out by a text-to-speech engine. "
    "You can speak and understand both Hindi and English (Hinglish too)."
)


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key nahi mili!)
else:         
genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    return jsonify({"status": "online", "assistant_name": "Maya", "creator": "Priyanshu Singh"})

@app.route('/api/ask', methods=['POST'])
def ask_maya():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"error": "Message is empty"}), 400
            
        # Gemini Model call kar rahe hain
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=MAYA_PERSONALITY
        )
        
        response = model.generate_content(user_message)
        maya_reply = response.text.strip()
        
        return jsonify({
            "success": True,
            "reply": maya_reply
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    # Render ya local host dono par chalne ke liye port dynamically uthayega
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
