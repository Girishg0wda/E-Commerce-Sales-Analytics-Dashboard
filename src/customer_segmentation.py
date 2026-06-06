import pandas as pd
from datetime import timedelta

df = pd.read_csv(
    "data/processed/cleaned_sales_data.csv"
)

df["Order Date"] = pd.to_datetime(
    df["Order Date"]
)

reference_date = (
    df["Order Date"].max()
    + timedelta(days=1)
)

rfm = df.groupby(
    "Customer Name"
).agg({
    "Order Date": lambda x:
        (reference_date - x.max()).days,
    "Order ID": "nunique",
    "Sales": "sum"
})

rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    4,
    labels=[4,3,2,1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1,2,3,4]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    4,
    labels=[1,2,3,4]
)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

def segment(score):

    score = int(score)

    if score >= 444:
        return "Champions"

    elif score >= 344:
        return "Loyal Customers"

    elif score >= 244:
        return "Potential Loyalists"

    else:
        return "Regular Customers"

rfm["Segment"] = (
    rfm["RFM_Score"]
    .astype(int)
    .apply(segment)
)

rfm.to_csv(
    "reports/customer_segments.csv"
)

print("\nCustomer Segments\n")
print(
    rfm["Segment"]
    .value_counts()
)