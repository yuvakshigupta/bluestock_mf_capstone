CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT,
sub_category TEXT,
expense_ratio_pct REAL,
risk_category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE,
year INTEGER,
month INTEGER,
quarter INTEGER,
is_weekday INTEGER
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
nav_date DATE,
nav REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL,
alpha REAL,
beta REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_house TEXT,
date DATE,
aum_crore REAL,
aum_lakh_crore REAL
);
