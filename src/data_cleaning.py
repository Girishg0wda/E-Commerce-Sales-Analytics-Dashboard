import pandas as pd


def load_data(path):
    return pd.read_csv(path, encoding="latin1")


def clean_data(df):
    df = df.drop_duplicates()

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month_Name"] = df["Order Date"].dt.month_name()

    return df


if __name__ == "__main__":
    df = load_data("data/raw/SampleSuperstore.csv")
    df = clean_data(df)

    df.to_csv(
        "data/processed/cleaned_sales_data.csv",
        index=False
    )

    print("Data cleaned successfully!")