import pandas as pd

CSV_PATH = "../data/cars.csv"


def task1_metadata_summary(df: pd.DataFrame) -> None:
    print("\n========== TASK 1: DATASET METADATA SUMMARY ==========")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn Names:")
    print(list(df.columns))
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values Per Column:")
    print(df.isna().sum())
    print("\nStatistical Summary (numeric columns):")
    print(df.describe(include="number"))
    print("======================================================\n")


def task2_missing_value_warning(df: pd.DataFrame, threshold: int = 5) -> None:
    print("\n========== TASK 2: MISSING VALUE WARNINGS ==========")
    missing_counts = df.isna().sum()
    flagged = False
    for col, count in missing_counts.items():
        if count > threshold:
            print(f"WARNING: '{col}' has {count} missing values (>{threshold})")
            flagged = True
    if not flagged:
        print(f"No columns have more than {threshold} missing values.")
    print("=====================================================\n")


def task3_validate_range(df: pd.DataFrame, column_name: str, min_value: float, max_value: float) -> None:
    print(f"\n========== TASK 3: RANGE VALIDATION ({column_name}) ==========")
    if column_name not in df.columns:
        print(f"ERROR: Column '{column_name}' not found.")
        print("=============================================================\n")
        return
    s = pd.to_numeric(df[column_name], errors="coerce")
    non_null = s.notna().sum()
    valid = s.between(min_value, max_value, inclusive="both").sum()
    invalid = non_null - valid
    print(f"Range: {min_value} to {max_value}")
    print(f"Non-null numeric values checked: {non_null}")
    print(f"Valid (within range): {valid}")
    print(f"Invalid (out of range): {invalid}")
    print("=============================================================\n")


def main():
    print("Loading dataset...")
    df = pd.read_csv(CSV_PATH)
    print("Loaded.\n")

    task1_metadata_summary(df)
    task2_missing_value_warning(df, threshold=5)

    print("Numeric columns detected:", df.select_dtypes(include="number").columns.tolist(), "\n")

    task3_validate_range(df, "MPG", 15, 55)
    task3_validate_range(df, "HP", 60, 200)


if __name__ == "__main__":
    main()
