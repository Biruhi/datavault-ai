def detect_file_type(df):

    columns = [

        str(col)
        .lower()

        for col
        in df.columns
    ]

    sales_keywords = [

        "revenue",
        "profit",
        "product",
        "region"
    ]

    invoice_keywords = [

        "invoice number",
        "vendor",
        "subtotal",
        "tax",
        "total"
    ]

    lead_keywords = [

        "company",
        "email",
        "phone",
        "city"
    ]

    if any(
        key in columns
        for key in sales_keywords
    ):
        return "sales"

    if any(
        key in columns
        for key in invoice_keywords
    ):
        return "invoice"

    if any(
        key in columns
        for key in lead_keywords
    ):
        return "lead"

    return "unknown"