import pandas as pd


def load_data(uploaded_file):

    filename = (
        uploaded_file.name
        .lower()
    )

    if filename.endswith(".csv"):

        return pd.read_csv(
            uploaded_file
        )

    if filename.endswith(".xlsx"):

        return pd.read_excel(
            uploaded_file
        )

    raise ValueError(
        "Unsupported file format"
    )