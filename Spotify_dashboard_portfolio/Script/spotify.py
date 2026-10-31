
# SPOTIFY DATA CLEANING PROJECT
import pandas as pd
import numpy as np

# STEP 1: Load the original CSV file
df = pd.read_csv("spotify_data.csv")

print("Original dataset shape:", df.shape)

# STEP 2: Inspect the dataset
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


# STEP 3: Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"\s+", "_", regex=True)
)

print("\nCleaned column names:")
print(df.columns.tolist())


# STEP 4: Remove extra spaces from text columns

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].astype("string").str.strip()


# STEP 5: Convert chart date to datetime

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

print("\nInvalid chart dates:", df["date"].isna().sum())


# STEP 6: Convert numeric columns
numeric_columns = [
    "position",
    "popularity",
    "duration_ms",
    "total_tracks"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    ).astype("Int64")


# STEP 7: Handle the explicit-content column

df["is_explicit"] = df["is_explicit"].astype("boolean")


# STEP 8: Standardize album type".

df["album_type"] = df["album_type"].str.lower()


# STEP 9: Handle release dates
df["release_year"] = pd.to_numeric(
    df["release_date"].str.extract(
        r"^(\d{4})",
        expand=False
    ),
    errors="coerce"
).astype("Int64")


# Parse only complete YYYY-MM-DD dates.
complete_dates = df["release_date"].where(
    df["release_date"].str.fullmatch(
        r"\d{4}-\d{2}-\d{2}"
    )
)

df["release_date_parsed"] = pd.to_datetime(
    complete_dates,
    format="%Y-%m-%d",
    errors="coerce"
)


# STEP 10: Remove exact duplicate rows
before_rows = len(df)

df = df.drop_duplicates()

removed_rows = before_rows - len(df)

print("\nDuplicate rows removed:", removed_rows)


# STEP 11: Create duration in minutes

df["duration_minutes"] = (
    df["duration_ms"] / 60000
).round(2)


# STEP 12: Validate the cleaned dataset
print("\nCleaned dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows remaining:", df.duplicated().sum())

print("\nFinal data types:")
print(df.dtypes)

print("\nSummary statistics:")
print(df.describe(include="all"))


# STEP 13: Save the cleaned dataset
df.to_csv("spotify_cleaned.csv", index=False)

print("\nCleaning completed successfully!")
print("Saved file: spotify_cleaned.csv")
