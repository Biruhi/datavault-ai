def analyze_sales(df):

    return {

        "Revenue":
        df["Revenue"].sum(),

        "Profit":
        df["Profit"].sum(),

        "Orders":
        len(df)
    }