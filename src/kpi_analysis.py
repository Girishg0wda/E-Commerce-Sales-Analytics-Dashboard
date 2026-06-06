import pandas as pd

df = pd.read_csv("data/processed/cleaned_sales_data.csv")

kpis = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Total Customers",
        "Average Order Value"
    ],
    "Value": [
        round(df["Sales"].sum(), 2),
        round(df["Profit"].sum(), 2),
        df["Order ID"].nunique(),
        df["Customer Name"].nunique(),
        round(df["Sales"].sum() / df["Order ID"].nunique(), 2)
    ]
})

kpis.to_csv(
    "reports/kpis.csv",
    index=False
)

print(kpis)