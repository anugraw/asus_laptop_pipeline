import os
import pandas as pd


def load_data(path=None):
    if path is None:
        # Get the repo root dynamically (works locally and in Actions)
        repo_root = os.getcwd()
        # Build absolute path to CSV file
        path = os.path.join(
            repo_root,
            "asus_laptops_cleaned_new.csv"
        )
        # If not found, try one folder up (for nested GitHub Actions)
        if not os.path.exists(path):
            path = os.path.join(
                repo_root,
                "..",
                "asus_laptops_cleaned_new.csv"
            )
    print("📁 Attempting to load dataset from:")
    print(os.path.abspath(path))
    # Load the CSV
    df = pd.read_csv(path)
    print(
        "✅ Data loaded successfully! "
        "Shape:",
        df.shape
    )
    return df


def basic_summary(df):
    print("📊 Dataset Summary:")
    print(df.describe())


if __name__ == "__main__":
    df = load_data()
    basic_summary(df)
