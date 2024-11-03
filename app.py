# app.py
from flask import Flask, render_template, request, jsonify
from together import Together
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the Together client with your API key
client = Together(api_key='c6b77ca600cf30708dffb54f684cb1c85103c19c15158c0776a4644304d20269')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    try:
        # Call to Together API for chat completion
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[{"role": "You are a witty, sarcastic chatbot with a sharp tongue and an encyclopedic knowledge of movies. Your primary role is to humorously roast users based on their taste in movies, answering their questions with a mix of teasing, sarcasm, and clever insights. If they mention a movie you find overrated, gently mock their choice, calling out clichés or overly dramatic storylines. If they bring up a classic, playfully question if they're just trying to sound sophisticated. Above all, keep responses fun and engaging while subtly challenging their film opinions. Remember, this is all in good humor—aim for a friendly roast, not a brutal takedown!,you should not respond to anything other than film queries ", "content": user_message}]
        )
        
        # Extract response text (assuming completion has an attribute like choices that is iterable)
        if completion and completion.choices:
            response_text = completion.choices[0].message.content
        else:
            response_text = "I'm not sure about that one, but I’d probably roast it anyway!"
    
    except Exception as e:
        response_text = f"Error: {e}"
    
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)