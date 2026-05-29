import pandas as pd
import numpy as np

from sklearn.linear_model import (
    LinearRegression
)


def forecast_revenue(df):

    if len(df) < 2:

        return None

    revenue_by_day = (

        df.groupby(
            "Date"
        )["Revenue"]
        .sum()
        .reset_index()

    )

    revenue_by_day[
        "Date"
    ] = pd.to_datetime(
        revenue_by_day[
            "Date"
        ]
    )

    revenue_by_day = (
        revenue_by_day
        .sort_values(
            "Date"
        )
    )

    X = np.arange(
        len(
            revenue_by_day
        )
    ).reshape(
        -1,
        1
    )

    y = revenue_by_day[
        "Revenue"
    ].values

    model = (
        LinearRegression()
    )

    model.fit(
        X,
        y
    )

    next_day = np.array(
        [[
            len(
                revenue_by_day
            )
        ]]
    )

    prediction = (
        model.predict(
            next_day
        )[0]
    )

    return {

        "Predicted Revenue":
        round(
            prediction,
            2
        )
    }