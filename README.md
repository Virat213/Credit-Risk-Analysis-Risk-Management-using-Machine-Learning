# Credit Risk Analysis and Risk Management using Machine Learning

This project focuses on predicting the credit risk of loan applicants using Machine Learning.

The model takes information such as age, income, employment length, loan amount, loan purpose, interest rate and credit history. Based on these details, it predicts whether an applicant is likely to be a low-risk or high-risk applicant.

It also provides the estimated probability of loan default.

**Live Project:**  
https://credit-risk-frontend-sepia.vercel.app/

**Backend API:**  
https://credit-risk-app-rs2h.onrender.com/

**API Documentation:**  
https://credit-risk-app-rs2h.onrender.com/docs


## What I did in this project

- Performed Exploratory Data Analysis (EDA).
- Cleaned and preprocessed the dataset.
- Handled missing values.
- Encoded categorical variables.
- Scaled numerical features.
- Trained and compared multiple Machine Learning models.
- Tuned the best-performing model using GridSearchCV.
- Used SHAP to understand model predictions.
- Created a frontend using HTML, CSS and JavaScript.
- Developed the backend using FastAPI.
- Used Docker for containerization.
- Deployed the frontend on Vercel and backend on Render.


## Dataset

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

The target variable is loan_status:

- 0 means no default.
- 1 means default.


## Machine Learning Models

I trained and compared the following classification models:

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

The models were evaluated using Accuracy, Precision, Recall, F1 Score, ROC-AUC and PR-AUC.

The best model based on ROC-AUC was selected and tuned using GridSearchCV.


## Data Preprocessing

For numerical columns, missing values were filled using the median and the features were scaled using StandardScaler.

For categorical columns, missing values were filled using the most frequent value and categorical values were converted using OneHotEncoder.

The trained model and preprocessing pipeline were saved using Joblib for making predictions on new applicant data.


## SHAP Explainability

I used SHAP to understand which features have the most influence on the model's predictions.

The project includes:

- SHAP summary plot
- Feature importance
- SHAP bar plot
- Individual applicant explanation
- SHAP waterfall plot

These visualizations help in understanding how different features contribute to a prediction.


## Frontend and Backend

The project uses a separate frontend and backend.

**Frontend:**

The frontend is developed using HTML, CSS and JavaScript. It provides a form where users can enter applicant information and view the prediction results.

**Backend:**

FastAPI is used to receive applicant information and communicate with the trained Machine Learning model.

The backend provides three main endpoints:

- GET / - Checks whether the API is running.
- GET /health - Checks the API health.
- POST /predict - Accepts applicant information and returns the predicted risk level and default probability.

The API documentation is available at:

https://credit-risk-app-rs2h.onrender.com/docs


## How the application works

1. The user enters applicant information on the website.
2. JavaScript sends the information to the FastAPI backend.
3. The backend processes the input using the saved preprocessing pipeline.
4. The trained XGBoost model makes a prediction.
5. The backend returns the risk level and default probability.
6. The frontend displays the result.


## Project Structure

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
├── frontend/
│   ├── index.html
│   └── static/
│       ├── background.png
│       ├── script.js
│       └── style.css
│
├── Dockerfile
├── requirements.txt
└── README.md


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript
- Docker
- Git and GitHub
- Render
- Vercel


## Running the Backend Locally

First clone the repository:

git clone https://github.com/Virat213/Credit-Risk-Analysis-Risk-Management-using-Machine-Learning.git

Move into the project directory:

cd Credit-Risk-Analysis-Risk-Management-using-Machine-Learning

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Start the FastAPI backend:

uvicorn api.main:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs


## Docker

The backend can also be run using Docker.

Build the image:

docker build -t credit-risk-app .

Run the container:

docker run -d -p 8000:8000 --name credit-risk-container credit-risk-app


## Deployment

The frontend and backend are deployed separately.

Frontend deployment: Vercel  
https://credit-risk-frontend-sepia.vercel.app/

Backend deployment: Render  
https://credit-risk-app-rs2h.onrender.com/

The frontend communicates with the backend through API requests.


## Limitations

This project is mainly developed for learning and demonstration purposes.

The predictions are estimates based on patterns learned from the training dataset. They are not guaranteed outcomes and should not be used as the only factor in real-world lending decisions.


## Future Improvements

- Try additional Machine Learning algorithms.
- Improve hyperparameter tuning.
- Add more financial features.
- Improve frontend validation.
- Add more detailed prediction explanations.
- Monitor model performance after deployment.


## Author

Virat Raj