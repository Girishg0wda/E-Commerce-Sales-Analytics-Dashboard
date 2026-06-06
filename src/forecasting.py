import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from pathlib import Path

Path("visuals").mkdir(exist_ok=True)

df = pd.read_csv(
    "data/processed/cleaned_sales_data.csv"
)

df["Order Date"] = pd.to_datetime(
    df["Order Date"]
)

sales = (
    df.groupby("Order Date")["Sales"]
      .sum()
      .reset_index()
)

sales.columns = ["ds", "y"]

model = Prophet()

model.fit(sales)

future = model.make_future_dataframe(
    periods=90
)

forecast = model.predict(future)

forecast[
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
].to_csv(
    "reports/forecast.csv",
    index=False
)

fig = model.plot(forecast)

plt.title("90-Day Sales Forecast")

plt.savefig(
    "visuals/forecast.png",
    bbox_inches="tight"
)

print("Forecast created successfully!")