def build_executive_summary(
    dataset_type,
    df
):

    summary = {}

    if dataset_type == "sales":

        summary = {

            "Revenue":
            round(
                df["Revenue"]
                .sum(),
                2
            ),

            "Profit":
            round(
                df["Profit"]
                .sum(),
                2
            ),

            "Orders":
            len(df)
        }

    elif dataset_type == "invoice":

        summary = {

            "Total Spend":
            round(
                df["Total"]
                .sum(),
                2
            ),

            "Vendors":
            df["Vendor"]
            .nunique(),

            "Invoices":
            len(df)
        }

    elif dataset_type == "lead":

        summary = {

            "Companies":
            len(df),

            "Cities":
            df["City"]
            .nunique(),

            "Emails":
            df["Email"]
            .count()
        }

    return summary