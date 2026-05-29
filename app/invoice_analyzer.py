def analyze_invoices(df):

    return {

        "Invoices":
        len(df),

        "Vendors":
        df["Vendor"]
        .nunique(),

        "Total Spend":
        df["Total"]
        .sum()
    }