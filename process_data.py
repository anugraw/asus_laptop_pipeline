import os
import pandas as pd


def load_data(path=None):
    # Dynamically build the correct path to the CSV file
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "asus_laptops_cleaned_new.csv")

    df = pd.read_csv(path)
    print(f"✅ Data loaded successfully! Shape: {df.shape}")
    return df


def basic_summary(df):
    print("📊 Dataset Summary:")
    print(df.describe())


if __name__ == "__main__":
    df = load_data()
    basic_summary(df)
