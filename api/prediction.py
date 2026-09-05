import os
import joblib
import pandas as pd


# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "credit_risk_model.pkl"
)

# Load trained model
model = joblib.load(MODEL_PATH)


def predict_credit_risk(applicant_data):
    """
    Predict credit default risk for a single applicant.

    Parameters:
        applicant_data (dict): Applicant information.

    Returns:
        dict: Prediction, probability and risk level.
    """

    # Convert input dictionary into DataFrame
    input_data = pd.DataFrame([applicant_data])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probability of default
    probability = model.predict_proba(input_data)[0][1]

    # Convert prediction into readable result
    if prediction == 1:
        risk_level = "High Risk"
    else:
        risk_level = "Low Risk"

    return {
        "prediction": int(prediction),
        "default_probability": round(float(probability), 4),
        "default_probability_percentage": round(float(probability) * 100, 2),
        "risk_level": risk_level
    }


if __name__ == "__main__":

    # Test applicant
    test_applicant = {
        "person_age": 25,
        "person_income": 50000,
        "person_home_ownership": "RENT",
        "person_emp_length": 3,
        "loan_intent": "EDUCATION",
        "loan_grade": "B",
        "loan_amnt": 10000,
        "loan_int_rate": 11.5,
        "loan_percent_income": 0.20,
        "cb_person_default_on_file": "N",
        "cb_person_cred_hist_length": 4
    }

    result = predict_credit_risk(test_applicant)

    print("Credit Risk Prediction")
    print("=" * 40)

    for key, value in result.items():
        print(f"{key}: {value}")