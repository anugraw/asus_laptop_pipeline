from process_data import load_data

def test_load_data():
    # Load the dataset using your function
    df = load_data()

    # ✅ Check 1: Dataset should not be empty
    assert not df.empty, "❌ Dataset is empty!"

    # ✅ Check 2: Expected key column should exist
    assert "Selling_Price_cleaned" in df.columns, "❌ Expected column 'Selling_Price_cleaned' not found!"

    # ✅ Check 3: Check for missing price values
    assert df["Selling_Price_cleaned"].notnull().all(), "❌ Missing values found in 'Selling_Price_cleaned' column!"

    # ✅ Check 4: Dataset should have at least 100 rows
    assert len(df) > 100, "❌ Dataset seems too small — expected >100 rows."
