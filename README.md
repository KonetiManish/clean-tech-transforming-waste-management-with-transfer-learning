Project Title: Healthy vs Rotten Classifier Web App

Description:
-------------
This project is a simple web application designed to classify fruits or vegetables as healthy or rotten using a trained machine learning model (`healthy_vs_rotten.h5`). It includes HTML templates for the frontend, static folders for uploaded files, and a Python backend (`app.py`).

Project Structure:
-------------------

app.py
Main Python Flask application to run the web server and handle requests.

healthy_vs_rotten.h5
Trained Keras model used to classify healthy vs. rotten produce.ipython.html
Optional: Exported HTML version of a Jupyter Notebook for model exploration.

Readme.txt
This file. Explains the purpose and structure of the project.

static/
assets/
CSS, JS, and image files for styling the website.
forms/
(Optional) Placeholder for uploaded or saved form data.
uploads/
Folder where user-uploaded images are stored for classification.

templates/
index.html
Homepage of the web app.
blog.html
Blog listing page.
blog-single.html
A single blog article page.
portfolio-details.html
A page showcasing project or model details.

How to Run:
-----------
1. Make sure Python and Flask are installed.
2. Place your trained `.h5` model file in the root directory.
3. Run the app:
   > python app.py
4. Visit `http://localhost:5000` in your browser.

Author:
--------
[K.Manish]
