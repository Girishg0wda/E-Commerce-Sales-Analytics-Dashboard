import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_sales_data.csv"
)

# Monthly Sales
monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
      .sum()
      .reset_index()
)

# Monthly Profit
monthly_profit = (
    df.groupby(["Year", "Month"])["Profit"]
      .sum()
      .reset_index()
)

# Top Products
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(20)
      .reset_index()
)

# Category Profitability
profitability = (
    df.groupby("Category")
      .agg({
          "Sales":"sum",
          "Profit":"sum"
      })
      .reset_index()
)

monthly_sales.to_csv(
    "reports/monthly_sales.csv",
    index=False
)

monthly_profit.to_csv(
    "reports/monthly_profit.csv",
    index=False
)

top_products.to_csv(
    "reports/top_products.csv",
    index=False
)

profitability.to_csv(
    "reports/profitability.csv",
    index=False
)

print("Dashboard datasets created.")