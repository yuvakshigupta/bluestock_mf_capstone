from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_DIR = BASE_DIR / "data" / "db"

engine = create_engine(
    f"sqlite:///{DB_DIR/'bluestock_mf.db'}"
)

# Load cleaned files

fund_df = pd.read_csv(
    PROCESSED_DIR / "clean_fund_master.csv"
)

nav_df = pd.read_csv(
    PROCESSED_DIR / "clean_nav_history.csv"
)

txn_df = pd.read_csv(
    PROCESSED_DIR / "clean_transactions.csv"
)

perf_df = pd.read_csv(
    PROCESSED_DIR / "clean_performance.csv"
)

aum_df = pd.read_csv(
    PROCESSED_DIR / "clean_aum.csv"
)

# Load into SQLite

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully.")