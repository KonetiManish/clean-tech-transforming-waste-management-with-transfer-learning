# Project Structure:
# clean tech : transforming waste management with transfer learning

# Technologies Used
1.Python 3.8+
2.TensorFlow / Keras
3.Flask (Backend)
4.Bootstrap 5 (Frontend)Project Title: Healthy vs Rotten Classifier Web App

# 🧠 Model Overview
1.Architecture: VGG16 (pre-trained on ImageNet)
2.Input Size: 224x224 RGB
3.Training: Custom dense layers for 3 classes
4.Framework: TensorFlow/Keras
# 📁 Project Structure
CleanTech/
 ├── app.py
 ├── healthy_vs_rotten.h5
 ├── train_model.py
 ├── dataset/
 │   ├── train/
 │   └── validation/
 ├── static/
 │   ├── uploads/
 │   └── assets/
 ├── templates/
 │   ├── index.html
 │   ├── blog.html
 │   ├── blog-single.html
 │   ├── portfolio-details.html
 │   └── ipython.html
 └── README.md
# 🛠️ Installation & Setup
git clone https://github.com/your-username/CleanTech-AI.git
cd CleanTech-AI
conda create -n cleantech python=3.8
conda activate cleantech
pip install -r requirements.txt
python train_model.py
python app.py
# 🌱 Dataset Format
Organize your dataset like this:
dataset/
├── train/
│   ├── biodegradable/
│   ├── recyclable/
│   └── trash/
└── validation/
    ├── biodegradable/
    ├── recyclable/
    └── trash/
        
Description:
-------------
This project is a simple web application designed to classify fruits or vegetables as healthy or rotten using a trained machine learning model (`healthy_vs_rotten.h5`). It includes HTML templates for the frontend, static folders for uploaded files, and a Python backend (`app.py`).

# app.py
Main Python Flask application to run the web server and handle requests
# healthy_vs_rotten.h5
Trained Keras model used to classify healthy vs. rotten produce.ipython.html
Optional: Exported HTML version of a Jupyter Notebook for model exploration.

This file. Explains the purpose and structure of the project.
# static/(assets,forms,uploaded images will go here)
# templates/(index.html,blog.html,blog single.html,portfolio-details.html)
# dataset/(train,validation,etc)
# Readme.md
🚀 How to Run the Application Ensure all setup steps are completed (prerequisites and installation).

Place your trained model file (trained_model.h5) directly in the C:\Clean Tech root directory, next to app.py.

Generate the Interactive Project Overview HTML: Run the conversion script to create templates/README_interactive_overview.html:

python convert_readme.py

Open Anaconda Prompt (as Administrator).

Navigate to your project's root directory:

cd C:\Clean Tech

Activate your Conda environment:

conda activate Clean_Tech # Or whatever you named your environment

Start the Flask application:

python app.py

You should see output similar to this, indicating the server is running and the model loaded:

✅ Model loaded successfully from C:\Clean Tech\trained_model.h5

Serving flask app "app" 

Debug mode: on
Running on all addresses (0.0.0.0)
Running on http://127.0.0.1:5000
Running on http://YOUR_LOCAL_IP:5000 Press CTRL+C to quit
💻 Usage Once the Flask application is running, open your web browser:
Blood Cell Classification Tool:
Go to http://127.0.0.1:5000/ (for access from your local machine).
If running on 0.0.0.0, others on your same local network can access it using your computer's local IP address (e.g., http://192.168.1.100:5000/).
On the page, click "Choose File", select a recycle,trash(or) Biodegradable Images (JPEG or PNG), and click "Classify Image" to see the prediction.
Interactive Project Overview (README):
Go to http://127.0.0.1:5000/project-overview in your browser.
This page provides a comprehensive, interactive overview of the project's details, features, and technical aspects.
🔮 Future Enhancements Advanced UI/UX: Implement more dynamic and visually engaging elements using JavaScript frameworks, potentially integrating a progress bar for uploads/predictions.
🤝 Contributing We welcome contributions to the Clean Tech ! If you have suggestions or improvements, please feel free to open an issue or submit a pull request (if this were a Git report).
Go to http://127.0.0.1:5000/project-overview in your brow

📄 License This project is licensed under the MIT License - see the LICENSE file for details (if you create one).
📧 Contact

How to Run:
-----------
1. Make sure Python and Flask are installed.
2. Place your trained `.h5` model file in the root directory.
3. Run the app:
   > python app.py
4. Visit `http://127.0.0.1:5000` in your browser.
5.
# TEAM ID:LTVIP2025TMID34776
# Project Lead:Hayath muhammad zaid Khan
# Team Members:jaswitha RV,K.Manish,K.Ramya
# Email: manishkoneti43@gmail.com
# Demo link: https://youtu.be/yDbGuqCchgg?si=QL9ufeG3PNrYTUZ9
# Smart Bridge Internship: [https://apsche.smartinternz.com/Student/guided_project_workspace/42645]
# License
This project is licensed under the MIT License.
