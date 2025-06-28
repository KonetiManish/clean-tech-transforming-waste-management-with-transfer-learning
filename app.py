from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = load_model('healthy_vs_rotten.h5')

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Upload folder path
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Class labels (index must match model training order)
class_names = ['Biodegradable', 'Recyclable', 'Trash']

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function: validate file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Blog overview
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Single blog post
@app.route('/blog-single')
def render_blog_single():
    return render_template('blog-single.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "⚠ No file part in request"
    
    file = request.files['file']
    
    if file.filename == '':
        return "⚠ No file selected"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess image
        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make prediction
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_class = class_names[predicted_index]

        # Render result page
        return render_template('portfolio-details.html', prediction=predicted_class, user_image=filepath)
    
    return "❌ Invalid file type. Please upload a JPG or PNG."

# Optional IPython-style result view
@app.route('/ipython')
def ipython():
    # Example test case
    return render_template('ipython.html', prediction="Trash", user_image="static/uploads/sample.jpg")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    