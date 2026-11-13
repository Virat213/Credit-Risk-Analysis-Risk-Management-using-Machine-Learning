
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from api.prediction import predict_credit_risk


app = FastAPI(
    title="Credit Risk Prediction API",
    description="A simple machine learning API for credit risk prediction",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/")
def home():
    return {
        "message": "Credit Risk Prediction API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(applicant: Applicant):

    applicant_data = applicant.model_dump()

    result = predict_credit_risk(applicant_data)

    return result
