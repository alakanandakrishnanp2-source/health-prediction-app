def predict_health_risk(glucose,
                        haemoglobin,
                        cholesterol):

    remarks = []

    if glucose >= 126:
        remarks.append(
            "Possible Diabetes Risk"
        )

    if haemoglobin < 12:
        remarks.append(
            "Possible Anaemia"
        )

    if cholesterol >= 240:
        remarks.append(
            "High Cholesterol Risk"
        )

    if not remarks:
        remarks.append(
            "No Significant Risk Detected"
        )

    return ", ".join(remarks)