
import streamlit as st

import pandas as pd
from database import (
    add_patient,
    view_patients,
    update_patient,
    delete_patient
    
)
from predictor import predict_health_risk
import re 
from datetime import date
from database import create_table

create_table()

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(
        re.match(pattern, email)
    )


def validate_dob(dob):
    return dob <= date.today()



# Application Title
st.title("Health Prediction Application")

# Patient Information Input Fields
full_name = st.text_input("Full Name")

dob = st.date_input(
    "Date of Birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

email = st.text_input(
    "Email Address"
)

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0
)

if st.button("Predict and Save"):

    # Name Validation
    if not full_name.strip():
        st.error(
            "Full Name cannot be empty."
        )

    # Email Validation
    elif not validate_email(email):
        st.error(
            "Please enter a valid email address."
        )

    # DOB Validation
    elif not validate_dob(dob):
        st.error(
            "Date of Birth cannot be a future date."
        )

    else:

        # Generate Prediction
        remarks = predict_health_risk(
            glucose,
            haemoglobin,
            cholesterol
        )

        # Save Patient
        add_patient(
            full_name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success(
            "Patient record saved successfully!"
        )

        st.write(
            "Prediction:",
            remarks
        )
        
st.subheader(
    "Patient Records"
)

patients = view_patients()

if patients:

    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Full Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info(
        "No patient records found."
    )

st.subheader("Update Patient")

update_id = st.number_input(
    "Patient ID to Update",
    min_value=1,
    step=1,
    key="update_id"
)
update_name = st.text_input(
    "New Full Name",
    key="update_name"
)

update_dob = st.date_input(
    "New Date of Birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    key="update_dob"
)

update_email = st.text_input(
    "New Email Address",
    key="update_email"
)

update_glucose = st.number_input(
    "New Glucose",
    min_value=0.0,
    key="update_glucose"
)

update_haemoglobin = st.number_input(
    "New Haemoglobin",
    min_value=0.0,
    key="update_haemoglobin"
)


update_cholesterol = st.number_input(
    "New Cholesterol",
    min_value=0.0,
    key="update_cholesterol"
)

if st.button("Update Patient"):

    if not update_name.strip():
        st.error("Full Name cannot be empty.")

    elif not validate_email(update_email):
        st.error("Please enter a valid email address.")

    elif not validate_dob(update_dob):
        st.error("Date of Birth cannot be a future date.")

    else:

        remarks = predict_health_risk(
            update_glucose,
            update_haemoglobin,
            update_cholesterol
        )

        rows = update_patient(
            update_id,
            update_name,
            str(update_dob),
            update_email,
            update_glucose,
            update_haemoglobin,
            update_cholesterol,
            remarks
        )

        if rows > 0:
            st.success(
                "Patient updated successfully!"
            )
        else:
            st.error(
                "Patient ID not found!"
            )

        st.rerun()


st.subheader("Delete Patient")

delete_id = st.number_input(
    "Patient ID to Delete",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.button("Delete Patient"):

    rows = delete_patient(delete_id)

    if rows > 0:
        st.success(
            "Patient deleted successfully!"
        )
    else:
        st.error(
            "Patient ID not found!"
        )

    st.rerun()

