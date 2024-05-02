from flask import Flask, request, jsonify, render_template
import logging
import google.generativeai as genai

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure the Gemini API key
genai.configure(api_key="AIzaSyA1LupTR0xsXYRqIHnGmYXC0h9D2Qr4slI")  

# Initialize the GenerativeModel with the appropriate model name
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data from the front-end
    age = request.form['age']
    interests = request.form['interests']
    food = request.form['food']
    budget = request.form['budget']
    duration = request.form['duration']
    attendees = request.form['attendees']

    # Generate the trip recommendation using the AI model
    try:
        response = model.generate_content(f"Age: {age}\nInterests: {interests}\nFood: {food}\nBudget: {budget}\nDuration: {duration}\nAttendees: {attendees}")
        # Extract text from the response
        recommendation = response.text
    except Exception as e:
        # Log the error
        logging.error(f'Error during generation: {str(e)}')
        # If an error occurs during generation, return an error response
        return jsonify({'response': f'Error: {str(e)}'})

    # Log the recommendation
    logging.info(f'Recommendation: {recommendation}')

    # Return the recommendation to the front-end
    return jsonify({'response': recommendation})

if __name__ == '__main__':
    app.run(debug=True)














