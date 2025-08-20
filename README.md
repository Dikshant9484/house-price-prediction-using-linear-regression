📈 Simple Linear Regression Predictor

This project is a web app that demonstrates a basic Linear Regression model using Scikit-learn and an interactive Streamlit UI.
It predicts the output y for a given input x using a pre-trained linear regression model.

🚀 Features

Trains a simple Linear Regression model on sample data.

Interactive Streamlit interface.

Enter a value for x and get the predicted value of y.

Displays model parameters (slope & intercept).

📂 Project Structure
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md           # Documentation

⚙️ Installation
1️⃣ Clone the repo
git clone https://github.com/your-username/simple-linear-regression-predictor.git
cd simple-linear-regression-predictor

2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, create one like:

streamlit
scikit-learn
numpy

▶️ Usage

Run the app:

streamlit run app.py
