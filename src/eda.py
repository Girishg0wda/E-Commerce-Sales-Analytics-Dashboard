def get_kpis(df):

    return {
        "sales": df["Sales"].sum(),
        "profit": df["Profit"].sum(),
        "orders": df["Order ID"].nunique(),
        "customers": df["Customer Name"].nunique()
    }