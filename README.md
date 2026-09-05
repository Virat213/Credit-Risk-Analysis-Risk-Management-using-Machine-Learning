# Credit Risk Analysis and Risk Management using Machine Learning

This project is about predicting the credit risk of a loan applicant using machine learning.

The model takes information such as the applicant's age, income, employment length, loan amount, loan purpose, loan grade and credit history. Based on these details, it predicts whether the applicant is likely to be a low-risk or high-risk applicant.

The project also shows the probability of default predicted by the model.

Live Project:
https://credit-risk-app-rs2h.onrender.com/


What I did in this project

- Performed Exploratory Data Analysis (EDA)
- Cleaned and preprocessed the dataset
- Handled missing values
- Encoded categorical variables
- Scaled numerical features
- Trained multiple machine learning models
- Compared the performance of the models
- Tuned the best model using GridSearchCV
- Used SHAP to understand model predictions
- Created a FastAPI backend
- Created a simple web interface using HTML, CSS and JavaScript
- Added Docker support
- Deployed the project using Render


Dataset

The dataset contains information about loan applicants and their loan details.

Some of the main columns are:

- person_age - Age of the applicant
- person_income - Annual income
- person_home_ownership - Home ownership status
- person_emp_length - Employment length
- loan_intent - Purpose of the loan
- loan_grade - Grade of the loan
- loan_amnt - Loan amount
- loan_int_rate - Interest rate
- loan_status - Target variable
- loan_percent_income - Loan amount compared to income
- cb_person_default_on_file - Previous default history
- cb_person_cred_hist_length - Length of credit history

The target variable is loan_status.

0 means no default and 1 means default.


Machine Learning Models

I trained and compared the following models:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

The models were compared using Accuracy, Precision, Recall, F1 Score, ROC-AUC and PR-AUC.

The best model based on ROC-AUC was then tuned using GridSearchCV.


Data Preprocessing

For numerical columns, missing values were filled using the median and the features were scaled using StandardScaler.

For categorical columns, missing values were filled using the most frequent value and categorical values were converted using OneHotEncoder.

The preprocessing steps and trained model were saved using Joblib so that the same processing can be used when making new predictions.


SHAP Explainability

I used SHAP to understand which features have the most effect on the model's predictions.

The project includes SHAP summary plots, feature importance and an individual applicant explanation using a SHAP waterfall plot.

This helps in understanding why the model predicts an applicant as higher or lower risk.


FastAPI

FastAPI is used as the backend of the project.

The main API endpoints are:

GET /

Used to check whether the application is running.

GET /health

Used as a simple health check.

POST /predict

Takes applicant information and returns the predicted risk level and default probability.

FastAPI also provides API documentation at:

/docs


Project Structure

Credit Risk/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── prediction.py
│
├── data/
│   ├── credit_risk_dataset.csv
│   └── credit_risk_cleaned.csv
│
├── model/
│   ├── preprocessor.pkl
│   ├── credit_risk_model.pkl
│   ├── model_comparison.csv
│   ├── feature_importance.csv
│   └── sample_prediction_explanation.csv
│
├── notebooks/
│   ├── Risk_Management.ipynb
│   ├── 01_eda.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_explainability.ipynb
│
├── static/
│   ├── background.png
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── Dockerfile
├── requirements.txt
└── README.md


Technologies Used

Python
Pandas
NumPy
Scikit-learn
XGBoost
SHAP
FastAPI
Uvicorn
HTML
CSS
JavaScript
Docker
GitHub
Render


How to run the project locally

First clone the repository:

git clone https://github.com/Virat213/Credit-Risk-Analysis-Risk-Management-using-Machine-Learning.git

Go to the project folder:

cd Credit-Risk-Analysis-Risk-Management-using-Machine-Learning

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Start the FastAPI application:

uvicorn api.main:app --reload

Then open:

http://127.0.0.1:8000

The API documentation is available at:

http://127.0.0.1:8000/docs


Docker

The project also includes a Dockerfile.

To build the Docker image:

docker build -t credit-risk-app .

To run the container:

docker run -d -p 8000:8000 --name credit-risk-container credit-risk-app

Then open:

http://localhost:8000


Deployment

The project is deployed using Render.

Live application:

https://credit-risk-app-rs2h.onrender.com/


Limitations

This project is mainly created for learning and demonstration purposes.

The prediction made by the model is only an estimate based on the patterns learned from the dataset. It should not be considered as a guaranteed result or used as the only factor for making real-world lending decisions.


Future Improvements

Some things that can be added in the future are:

- More machine learning models
- Better hyperparameter tuning
- More financial features
- Better frontend validation
- More detailed prediction explanations
- Model performance monitoring


Author

Virat Raj