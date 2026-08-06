# ---------------------------------------------------------
# Import Required Libraries
# ---------------------------------------------------------

# Streamlit is used to create the web application interface.
import streamlit as st

# Joblib is used to load the trained machine learning model.
import joblib

# Pandas is used to create a DataFrame for model prediction.
import pandas as pd


# ---------------------------------------------------------
# Configure Streamlit Page
# ---------------------------------------------------------

# Set the page title, browser icon, and layout of the web application.
st.set_page_config(
    page_title="Health Insurance Cost Prediction",
    page_icon="💰",
    layout="centered"
)


# ---------------------------------------------------------
# Load the Trained Machine Learning Model
# ---------------------------------------------------------

# Load the saved Gradient Boosting Regression model from the local file.
model = joblib.load("model/model_joblib_gr1")


# ---------------------------------------------------------
# Display Application Title and Description
# ---------------------------------------------------------

# Display the main heading of the application.
st.title("🏥 Health Insurance Cost Prediction")

# Display a short description for the user.
st.write(
    "Enter the patient's details below to estimate the health insurance cost."
)

# Add a horizontal divider for better UI.
st.divider()


# ---------------------------------------------------------
# Collect User Input
# ---------------------------------------------------------

# Input patient's age.
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

# Select patient's gender.
sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

# Input Body Mass Index (BMI).
bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

# Input number of children covered under insurance.
children = st.number_input(
    "Children",
    min_value=0,
    max_value=10,
    value=0
)

# Select smoking status.
smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

# Select residential region.
region = st.selectbox(
    "Region",
    [
        "Southwest",
        "Southeast",
        "Northwest",
        "Northeast"
    ]
)


# ---------------------------------------------------------
# Convert Categorical Data into Numerical Values
# ---------------------------------------------------------

# Convert Gender into numerical format.
# Male = 1
# Female = 0
sex = 1 if sex == "Male" else 0


# Convert Smoking Status into numerical format.
# According to the notebook encoding:
# Yes = 0
# No = 1
smoker = 0 if smoker == "Yes" else 1


# Create a dictionary to convert region names into numerical values.
region_dict = {
    "Southwest": 1,
    "Southeast": 2,
    "Northwest": 3,
    "Northeast": 4
}

# Replace the selected region with its encoded value.
region = region_dict[region]


# ---------------------------------------------------------
# Predict Insurance Cost
# ---------------------------------------------------------

# Execute prediction only when the user clicks the button.
if st.button("Predict Insurance Cost", use_container_width=True):

    # Create a DataFrame containing all user inputs.
    # The column names must match the columns used during model training.
    input_data = pd.DataFrame(
        [[age, sex, bmi, children, smoker, region]],
        columns=[
            "age",
            "sex",
            "bmi",
            "children",
            "smoker",
            "region"
        ]
    )

    # Use the trained model to predict the insurance cost.
    prediction = model.predict(input_data)

    # Display the predicted insurance cost.
    st.success(
        f"Estimated Health Insurance Cost: ${prediction[0]:,.2f}"
    )