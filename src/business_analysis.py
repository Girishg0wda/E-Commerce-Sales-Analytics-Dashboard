import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_sales_data.csv"
)

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .reset_index()
)

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .reset_index()
)

top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

category_sales.to_csv(
    "reports/category_sales.csv",
    index=False
)

region_sales.to_csv(
    "reports/region_sales.csv",
    index=False
)

top_customers.to_csv(
    "reports/top_customers.csv",
    index=False
)

print("Business reports generated.")