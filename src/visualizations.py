import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

Path("visuals").mkdir(exist_ok=True)

df = pd.read_csv("data/processed/cleaned_sales_data.csv")

# Category Sales
category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(8,5))
sns.barplot(data=category_sales,
            x="Category",
            y="Sales")

plt.title("Sales by Category")
plt.tight_layout()

plt.savefig("visuals/category_sales.png")
plt.close()

# Region Sales
region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(8,5))
sns.barplot(data=region_sales,
            x="Region",
            y="Sales")

plt.title("Sales by Region")
plt.tight_layout()

plt.savefig("visuals/region_sales.png")
plt.close()

print("Visualizations generated successfully!")