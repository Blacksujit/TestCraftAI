from flask import Blueprint, render_template, request, jsonify
import os
from .utils import query_huggingface_api

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = request.form.get('context')
        images = request.files.getlist('images')

        results = []
        for image in images:
            image_path = os.path.join('app/static/uploads', image.filename)
            image.save(image_path)
            result = query_huggingface_api(image_path, context)
            results.append(result)

        return jsonify(results)

    return render_template('index.html')
