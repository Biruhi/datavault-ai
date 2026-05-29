def analyze_leads(df):

    return {

        "Companies":
        len(df),

        "Cities":
        df["City"]
        .nunique(),

        "Emails":
        df["Email"]
        .count()
    }