# Pandas — Titanic Dataset Clean & Analyze

End-to-end mini project applying core Pandas skills: cleaning a real dataset 
and analyzing survival patterns.

## What this covers

- **Loading & inspecting** — checking shape, dtypes, and missing values
- **Cleaning** — handling nulls in `Age`, `Fare`, and `Cabin` with different 
  strategies depending on how much data was missing and what the column meant
- **Feature engineering** — bucketing continuous `Age` into categories 
  (child/teenager/adult/senior citizen) using `pd.cut()`
- **Groupby analysis** — survival rate by passenger class, gender, and age group

## Files

- `titanic-dataset-clean-analyze.ipynb` — full notebook: cleaning, feature 
  engineering, groupby analysis, and written findings

## Key findings

- First-class passengers had a notably higher survival rate (~46%) than 
  third-class (~33%)
- Senior citizens had a somewhat higher survival rate (~39%) than adults (~33%), 
  which was unexpected
- Gender split in this file showed 100% survival for females and 0% for males — 
  likely reflecting the nature of this particular data source rather than 
  genuine mixed outcomes, a good reminder to verify what a dataset represents 
  before drawing conclusions

## Key takeaways

- For columns with too much missing data to safely fill (like `Cabin`), 
  dropping or converting to a binary "known/unknown" flag is often better 
  than filling with mode, which can fabricate misleading data
- `pd.cut()` needs one more bin edge than labels
