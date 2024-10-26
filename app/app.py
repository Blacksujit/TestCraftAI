from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from utils.llm import generate_test_instructions
import os

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/uploads/'  # Directory for uploaded images
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16 MB

# Set Hugging Face cache directory
os.environ["HF_HOME"] = "D:/huggingface_cache"  # Change to a path with more space

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Serve the HTML form

@app.route('/api/describe-instructions', methods=['POST'])
def describe_instructions():
    # Get the optional context from the form
    context = request.form.get('context', '')
    images = request.files.getlist('images')

    # Save uploaded images
    image_paths = []
    for image in images:
        if image.filename != '':
            filename = secure_filename(image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            image_paths.append(path)

    # Generate test instructions using the LLM API
    try:
        instructions = generate_test_instructions(context, image_paths)
        return jsonify({"instructions": instructions}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
