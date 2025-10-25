import os
import pandas as pd


def load_data(path=None):
    if path is None:
        # Get the current working directory
        repo_root = os.getcwd()

        # Try locating the dataset in common locations
        possible_paths = [
            os.path.join(repo_root, "asus_laptops_cleaned_new.csv"),
            os.path.join(repo_root, "..", "asus_laptops_cleaned_new.csv"),
            os.path.join(repo_root, "data", "asus_laptops_cleaned_new.csv")
        ]

        # Pick the first file that exists
        path = next((p for p in possible_paths if os.path.exists(p)), None)

        if not path:
            raise FileNotFoundError(
                "❌ Dataset 'asus_laptops_cleaned_new.csv' "
                "not found in expected paths!"
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
