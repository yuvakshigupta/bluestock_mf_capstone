from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

datasets = {
    "fund_master":"01_fund_master.csv",
    "nav_history":"02_nav_history.csv",
    "aum":"03_aum_by_fund_house.csv",
    "sip":"04_monthly_sip_inflows.csv",
    "category":"05_category_inflows.csv",
    "folio":"06_industry_folio_count.csv",
    "performance":"07_scheme_performance.csv",
    "transactions":"08_investor_transactions.csv",
    "holdings":"09_portfolio_holdings.csv",
    "benchmark":"10_benchmark_indices.csv"
}

summary = []

for name,file in datasets.items():

    df = pd.read_csv(RAW_DIR / file)

    print("="*60)
    print(name.upper())

    print("Shape")
    print(df.shape)

    print("Dtypes")
    print(df.dtypes)

    print("Head")
    print(df.head())

    print("Missing Values")
    print(df.isnull().sum())

    print("Duplicates")
    print(df.duplicated().sum())

    summary.append({
        "dataset": name,
        "rows": len(df),
        "columns": len(df.columns),
        "nulls": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum()
    })


summary_df = pd.DataFrame(summary)

summary_df.to_csv(
    PROCESSED_DIR / "data_quality_summary.csv",
    index=False
)

fund_df = pd.read_csv(
    RAW_DIR / "01_fund_master.csv"
)

print(fund_df["fund_house"].unique())
print(fund_df["category"].unique())
print(fund_df["sub_category"].unique())
print(fund_df["risk_category"].value_counts())


nav_df = pd.read_csv(
    RAW_DIR / "02_nav_history.csv"
)

fund_codes = set(
    fund_df["amfi_code"]
)

nav_codes = set(
    nav_df["amfi_code"]
)

missing_codes = fund_codes - nav_codes

print(missing_codes)

