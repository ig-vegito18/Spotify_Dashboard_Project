# Spotify Chart Data Analysis

## Project Overview

This beginner-friendly data analytics project uses Python and Pandas to clean and explore Spotify chart data. The goal is to prepare the dataset for analysis, investigate chart performance, and communicate findings through clear visualizations.

## Objectives

- Inspect the dataset and assess data quality.
- Standardize column names and text formatting.
- Convert columns to suitable data types.
- Review duplicate records and validate key fields.
- Explore chart rankings, artist appearances, popularity, and track duration.
- Create visualizations and summarize evidence-based findings.

## Dataset

- **Raw file:** `spotify_data.csv`
- **Records:** 27,800
- **Original columns:** 11
- **Chart date range:** May 18, 2023 to November 27, 2024

The dataset includes chart date, chart position, song, artist, Spotify popularity, track duration, album type, total tracks, release date, explicit-content status, and album-cover URL.

> Data note: the chart dataset contains repeated song appearances across dates, which are not automatically duplicates. Some release dates have only year or year-month precision, so incomplete dates should not be assigned an invented day.

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
Spotify-Data-Analysis-Project/
├── README.md
├── data/
│   ├── spotify_data.csv
│   └── spotify_cleaned.csv
├── notebooks/
│   └── spotify_analysis.ipynb
├── scripts/
│   └── clean_spotify.py
└── visuals/
    └── (exported charts and screenshots)
```

## Workflow

1. **Load and inspect:** review the first rows, shape, column types, summary statistics, missing values, and exact duplicates.
2. **Standardize:** trim text whitespace and normalize column names.
3. **Convert data types:** parse chart dates, convert numeric columns, and represent the explicit-content flag as a Boolean.
4. **Handle release dates carefully:** preserve the original release-date text, extract the release year where possible, and parse complete dates without inventing missing date components.
5. **Check duplicates:** remove exact duplicate rows only after reviewing the dataset's structure.
6. **Create useful fields:** convert track duration from milliseconds to minutes.
7. **Validate and analyze:** check ranges, summarize chart performance, and create visualizations.
8. **Document findings:** report only conclusions supported by analysis.

## Cleaning Results

The initial inspection and cleaning run found:

- 27,800 records in the raw dataset.
- 11 original columns; 3 derived columns were added, resulting in 14 columns.
- No initially missing values.
- No exact duplicate rows removed.
- No invalid chart dates after conversion.
- 105 records without a complete `YYYY-MM-DD` release date; their original values are preserved.

The added columns are:

- `release_year` — the year extracted from the original release-date text when available.
- `release_date_parsed` — a parsed date only when a complete valid `YYYY-MM-DD` date is present.
- `duration_minutes` — track duration in minutes, rounded to two decimal places.

These results describe data-processing checks, not proof that every record is factually correct. Further validation and analysis are still recommended.

## Questions for Exploratory Data Analysis

- Which songs most frequently appear at chart position 1?
- Which artists have the most chart appearances?
- How do chart positions change over time?
- Is Spotify popularity associated with chart position?
- How do chart-position distributions compare for explicit and non-explicit tracks?
- What does the distribution of track durations look like?

When counting artists, note that collaborations may appear as a single combined artist string unless artist names are split and normalized.

## Visualizations to Include

Recommended charts:

1. Bar chart of most frequent artists or artist appearances in the top 10.
2. Line chart of chart performance over time.
3. Scatter plot of popularity versus chart position.
4. Box plot comparing chart positions for explicit and non-explicit tracks.
5. Histogram of track durations.

Give each chart a clear title, labeled axes, and a short explanation. Avoid claiming that an association proves causation.

## How to Run

1. Place the raw CSV at `data/spotify_data.csv` (or update the path in the code).
2. Install the libraries listed in `requirements.txt`.
3. Run `scripts/clean_spotify.py` to create `data/spotify_cleaned.csv`, or run the cleaning cells in the notebook.
4. Open `notebooks/spotify_analysis.ipynb` and run the cells from top to bottom.
5. Save charts to the `visuals/` folder and add verified findings to this README.

## Limitations

- Chart position is a rank; a smaller number represents a better position.
- Spotify popularity and chart position are different measures.
- Repeated appearances across dates are expected and should not be removed as duplicates automatically.
- Incomplete release dates are retained as supplied; the exact release day cannot be inferred from a year or year-month value.
- Artist collaborations may require additional parsing for per-artist counts.
- Findings should be treated as descriptive unless a suitable causal design is used.

## Conclusion

This project demonstrates a reproducible workflow for data inspection, cleaning, validation, exploratory analysis, and visualization using Python. The final conclusions will be based on the measured patterns found in the notebook.
