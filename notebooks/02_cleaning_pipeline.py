from pathlib import Path
import pandas as pd

# =====================================================
# PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("DAY 2 - DATA CLEANING PIPELINE")
print("=" * 60)

# =====================================================
# LOAD DATASETS
# =====================================================

fund_df = pd.read_csv(RAW_DIR / "01_fund_master.csv")
nav_df = pd.read_csv(RAW_DIR / "02_nav_history.csv")
aum_df = pd.read_csv(RAW_DIR / "03_aum_by_fund_house.csv")
sip_df = pd.read_csv(RAW_DIR / "04_monthly_sip_inflows.csv")
category_df = pd.read_csv(RAW_DIR / "05_category_inflows.csv")
folio_df = pd.read_csv(RAW_DIR / "06_industry_folio_count.csv")
perf_df = pd.read_csv(RAW_DIR / "07_scheme_performance.csv")
txn_df = pd.read_csv(RAW_DIR / "08_investor_transactions.csv")
holdings_df = pd.read_csv(RAW_DIR / "09_portfolio_holdings.csv")
benchmark_df = pd.read_csv(RAW_DIR / "10_benchmark_indices.csv")

print("\nDatasets loaded successfully.")

# =====================================================
# CLEAN NAV HISTORY
# =====================================================

print("\nCleaning NAV History...")

nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    format="mixed"
)

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

nav_df = nav_df.drop_duplicates()

# Validate NAV > 0
invalid_nav = nav_df[nav_df["nav"] <= 0]

print(f"Invalid NAV rows: {len(invalid_nav)}")

# Forward fill weekends/holidays
clean_nav = []

for amfi_code, group in nav_df.groupby("amfi_code"):

    group = group.set_index("date")

    full_dates = pd.date_range(
        start=group.index.min(),
        end=group.index.max(),
        freq="D"
    )

    group = group.reindex(full_dates)

    group["amfi_code"] = amfi_code

    group["nav"] = group["nav"].ffill()

    group = group.reset_index()

    group.rename(
        columns={"index": "date"},
        inplace=True
    )

    clean_nav.append(group)

nav_df = pd.concat(
    clean_nav,
    ignore_index=True
)

print("NAV cleaning completed.")

# =====================================================
# CLEAN TRANSACTIONS
# =====================================================

print("\nCleaning Transactions...")

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"],
    format="mixed",
    errors="coerce"
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

invalid_types = txn_df[
    ~txn_df["transaction_type"].isin(valid_types)
]

print(
    f"Invalid transaction types: {len(invalid_types)}"
)

txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

print(
    f"Transactions after amount validation: {len(txn_df)}"
)

print("\nTransaction Types")
print(
    txn_df["transaction_type"]
    .value_counts()
)

print("\nKYC Status")
print(
    txn_df["kyc_status"]
    .value_counts()
)

# =====================================================
# CLEAN PERFORMANCE
# =====================================================

print("\nCleaning Performance Dataset...")

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

print("\nExpense Ratio Summary")
print(
    perf_df["expense_ratio_pct"]
    .describe()
)

expense_anomalies = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1)
    |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print(
    f"\nExpense Ratio Anomalies: {len(expense_anomalies)}"
)

negative_returns = perf_df[
    perf_df["return_1yr_pct"] < -100
]

print(
    f"Extreme Return Anomalies: {len(negative_returns)}"
)

# =====================================================
# FUND MASTER VALIDATION
# =====================================================

print("\nFund Master Validation")

print("\nFund Houses")
print(
    fund_df["fund_house"]
    .nunique()
)

print("\nCategories")
print(
    fund_df["category"]
    .unique()
)

print("\nSub Categories")
print(
    fund_df["sub_category"]
    .unique()
)

print("\nRisk Categories")
print(
    fund_df["risk_category"]
    .value_counts()
)

# =====================================================
# AMFI CODE VALIDATION
# =====================================================

print("\nAMFI Code Validation")

fund_codes = set(
    fund_df["amfi_code"]
)

nav_codes = set(
    nav_df["amfi_code"]
)

missing_codes = (
    fund_codes - nav_codes
)

print(
    f"Missing AMFI Codes: {len(missing_codes)}"
)

print(missing_codes)

# =====================================================
# CLEAN REMAINING DATASETS
# =====================================================

print("\nCleaning Remaining Datasets...")

aum_df["date"] = pd.to_datetime(
    aum_df["date"],
    format="mixed",
    errors="coerce"
)

sip_df["month"] = pd.to_datetime(
    sip_df["month"],
    format="mixed",
    errors="coerce"
)

category_df["month"] = pd.to_datetime(
    category_df["month"],
    format="mixed",
    errors="coerce"
)

folio_df["month"] = pd.to_datetime(
    folio_df["month"],
    format="mixed",
    errors="coerce"
)

benchmark_df["date"] = pd.to_datetime(
    benchmark_df["date"],
    format="mixed",
    errors="coerce"
)

holdings_df["portfolio_date"] = pd.to_datetime(
    holdings_df["portfolio_date"],
    format="mixed",
    errors="coerce"
)

# =====================================================
# SAVE CLEANED FILES
# =====================================================

print("\nSaving cleaned datasets...")

fund_df.to_csv(
    PROCESSED_DIR / "clean_fund_master.csv",
    index=False
)

nav_df.to_csv(
    PROCESSED_DIR / "clean_nav_history.csv",
    index=False
)

aum_df.to_csv(
    PROCESSED_DIR / "clean_aum.csv",
    index=False
)

sip_df.to_csv(
    PROCESSED_DIR / "clean_sip.csv",
    index=False
)

category_df.to_csv(
    PROCESSED_DIR / "clean_category.csv",
    index=False
)

folio_df.to_csv(
    PROCESSED_DIR / "clean_folio.csv",
    index=False
)

perf_df.to_csv(
    PROCESSED_DIR / "clean_performance.csv",
    index=False
)

txn_df.to_csv(
    PROCESSED_DIR / "clean_transactions.csv",
    index=False
)

holdings_df.to_csv(
    PROCESSED_DIR / "clean_holdings.csv",
    index=False
)

benchmark_df.to_csv(
    PROCESSED_DIR / "clean_benchmark.csv",
    index=False
)

print("\nAll cleaned files saved.")

# =====================================================
# SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("DAY 2 CLEANING COMPLETE")
print("=" * 60)

print(f"Fund Master: {len(fund_df):,}")
print(f"NAV History: {len(nav_df):,}")
print(f"Transactions: {len(txn_df):,}")
print(f"Performance: {len(perf_df):,}")

print("\nProcessed files saved in:")
print(PROCESSED_DIR)