from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from api.prediction import predict_credit_risk

import os


# Project directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Create FastAPI application
app = FastAPI(
    title="Credit Risk Prediction API",
    description="A simple machine learning API for credit risk prediction",
    version="1.0"
)


# Serve CSS and JavaScript files
app.mount(
    "/static",
    StaticFiles(
        directory=os.path.join(BASE_DIR, "static")
    ),
    name="static"
)


# Input data model
class Applicant(BaseModel):

    person_age: int = Field(..., ge=18)

    person_income: float = Field(..., gt=0)

    person_home_ownership: str

    person_emp_length: float = Field(..., ge=0)

    loan_intent: str

    loan_grade: str

    loan_amnt: float = Field(..., gt=0)

    loan_int_rate: float = Field(..., gt=0)

    loan_percent_income: float = Field(..., ge=0)

    cb_person_default_on_file: str

    cb_person_cred_hist_length: float = Field(..., ge=0)


# Home page
@app.get("/", response_class=HTMLResponse)
def home():

    html_path = os.path.join(
        BASE_DIR,
        "templates",
        "index.html"
    )

    with open(html_path, "r", encoding="utf-8") as file:
        return file.read()


# Health check
@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# Prediction endpoint
@app.post("/predict")
def predict(applicant: Applicant):

    applicant_data = applicant.model_dump()

    result = predict_credit_risk(
        applicant_data
    )

    return result