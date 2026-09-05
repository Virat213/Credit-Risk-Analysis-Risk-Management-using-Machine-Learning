const form = document.getElementById("predictionForm");
const resultDiv = document.getElementById("result");
const predictButton = document.getElementById("predictButton");


form.addEventListener("submit", async function (event) {

    event.preventDefault();

    // Collect form data
    const applicantData = {
        person_age: Number(
            document.getElementById("person_age").value
        ),

        person_income: Number(
            document.getElementById("person_income").value
        ),

        person_home_ownership:
            document.getElementById("person_home_ownership").value,

        person_emp_length: Number(
            document.getElementById("person_emp_length").value
        ),

        loan_intent:
            document.getElementById("loan_intent").value,

        loan_grade:
            document.getElementById("loan_grade").value,

        loan_amnt: Number(
            document.getElementById("loan_amnt").value
        ),

        loan_int_rate: Number(
            document.getElementById("loan_int_rate").value
        ),

        loan_percent_income: Number(
            document.getElementById("loan_percent_income").value
        ),

        cb_person_default_on_file:
            document.getElementById(
                "cb_person_default_on_file"
            ).value,

        cb_person_cred_hist_length: Number(
            document.getElementById(
                "cb_person_cred_hist_length"
            ).value
        )
    };


    // Disable button while prediction is running
    predictButton.disabled = true;
    predictButton.textContent = "Predicting...";


    // Show loading message
    resultDiv.innerHTML = `
        <h2>Prediction Result</h2>
        <p>Analyzing applicant information...</p>
    `;


    try {

        // Send applicant data to FastAPI
        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(applicantData)

        });


        // Handle API errors
        if (!response.ok) {

            throw new Error(
                "Prediction request failed."
            );

        }


        // Read API response
        const result = await response.json();


        // Decide result styling
        let riskClass = "";

        if (result.risk_level === "Low Risk") {

            riskClass = "risk-low";

        } else {

            riskClass = "risk-high";

        }


        // Display prediction
        resultDiv.innerHTML = `

            <h2>Prediction Result</h2>

            <p>
                <strong>Risk Level:</strong>
            </p>

            <p class="${riskClass}">
                ${result.risk_level}
            </p>

            <p>
                <strong>Default Probability:</strong>
            </p>

            <p>
                ${result.default_probability_percentage}%
            </p>

        `;


    } catch (error) {

        // Display error
        resultDiv.innerHTML = `

            <h2>Prediction Error</h2>

            <p>
                Unable to get prediction.
                Please check that the API is running
                and try again.
            </p>

        `;

        console.error(error);

    }


    // Enable button again
    predictButton.disabled = false;
    predictButton.textContent = "Predict Credit Risk";

});