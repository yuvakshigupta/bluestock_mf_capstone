# Day 1 Data Quality Report

## Project Information

**Project:** Mutual Fund Analytics Platform
**Organization:** Bluestock Fintech Pvt. Ltd.
**Phase:** Day 1 – Project Setup & Data Ingestion (ETL)
**Prepared By:** Yuvakshi Gupta
**Date:** June 2026

---

# 1. Objective

The objective of Day 1 was to:

- Set up the project environment and folder structure
- Load and validate all provided datasets
- Explore the Mutual Fund master dataset
- Verify AMFI code consistency across datasets
- Fetch live NAV data from mfapi.in
- Generate an initial data quality assessment

---

# 2. Dataset Summary

| Dataset               |   Rows | Columns | Null Values | Duplicates |
| --------------------- | -----: | ------: | ----------: | ---------: |
| Fund Master           |     40 |      15 |           0 |          0 |
| NAV History           | 46,000 |       3 |           0 |          0 |
| AUM by Fund House     |     90 |       5 |           0 |          0 |
| Monthly SIP Inflows   |     48 |       6 |          12 |          0 |
| Category Inflows      |    144 |       3 |           0 |          0 |
| Industry Folio Count  |     21 |       6 |           0 |          0 |
| Scheme Performance    |     40 |      19 |           0 |          0 |
| Investor Transactions | 32,778 |      13 |           0 |          0 |
| Portfolio Holdings    |    322 |       8 |           0 |          0 |
| Benchmark Indices     |  8,050 |       3 |           0 |          0 |

### Summary Statistics

- Total datasets loaded: 10
- Total records analysed: 87,533
- Total missing values: 12
- Total duplicate records: 0

All datasets were successfully loaded into Pandas and passed initial validation checks.

## Fund Master Exploration

### Fund Houses Identified

1. SBI Mutual Fund
2. HDFC Mutual Fund
3. ICICI Prudential MF
4. Nippon India MF
5. Kotak Mahindra MF
6. Axis Mutual Fund
7. Aditya Birla Sun Life MF
8. UTI Mutual Fund
9. Mirae Asset MF
10. DSP Mutual Fund

Total Fund Houses: 10

### Categories

- Equity
- Debt

Total Categories: 2

### Key Observation

The Fund Master dataset contains 40 mutual fund schemes distributed across 10 major Asset Management Companies (AMCs). The dataset provides scheme metadata including AMFI code, category, benchmark, expense ratio, risk category, and fund manager information.

# 3. Missing Value Analysis

| Dataset               | Missing Values |
| --------------------- | -------------: |
| Fund Master           |              0 |
| NAV History           |              0 |
| AUM by Fund House     |              0 |
| Monthly SIP Inflows   |             12 |
| Category Inflows      |              0 |
| Industry Folio Count  |              0 |
| Scheme Performance    |              0 |
| Investor Transactions |              0 |
| Portfolio Holdings    |              0 |
| Benchmark Indices     |              0 |

## Observation

The Monthly SIP Inflows dataset contains **12 missing values** in the `yoy_growth_pct` column.

This is expected because Year-over-Year growth cannot be calculated for the initial months where historical comparison data is unavailable.

No corrective action is required at this stage.

---

# 4. Duplicate Record Analysis

| Dataset               | Duplicate Records |
| --------------------- | ----------------: |
| Fund Master           |                 0 |
| NAV History           |                 0 |
| AUM by Fund House     |                 0 |
| Monthly SIP Inflows   |                 0 |
| Category Inflows      |                 0 |
| Industry Folio Count  |                 0 |
| Scheme Performance    |                 0 |
| Investor Transactions |                 0 |
| Portfolio Holdings    |                 0 |
| Benchmark Indices     |                 0 |

## Observation

No duplicate records were found in any dataset.

---

# 5. Fund Master Exploration

## Unique Fund Houses

The Fund Master dataset contains the following Asset Management Companies (AMCs):

1. SBI Mutual Fund
2. HDFC Mutual Fund
3. ICICI Prudential MF
4. Nippon India MF
5. Kotak Mahindra MF
6. Axis Mutual Fund
7. Aditya Birla Sun Life MF
8. UTI Mutual Fund
9. Mirae Asset MF
10. DSP Mutual Fund

Total Fund Houses: **10**

---

## Categories Identified

- Equity
- Debt

Total Categories: **2**

---

## Risk Categories

The dataset contains schemes across multiple risk profiles including:

- Low
- Moderate
- High
- Very High

---

## AMFI Scheme Codes

The Fund Master dataset contains unique AMFI codes for all schemes.

Examples:

| AMFI Code | Fund                           |
| --------- | ------------------------------ |
| 119551    | SBI Bluechip Fund              |
| 120503    | ICICI Prudential Bluechip Fund |
| 125497    | HDFC Top 100 Fund              |
| 118632    | Nippon India Large Cap Fund    |
| 119092    | Axis Bluechip Fund             |

These AMFI codes act as primary identifiers for joining fund-related datasets.

---

# 6. NAV History Assessment

## NAV Dataset Statistics

- Total NAV Records: 46,000
- Missing NAV Values: 0
- Duplicate Records: 0

## Observation

The NAV dataset is complete and suitable for future return calculations, volatility analysis, risk metrics, and benchmark comparisons.

For subsequent ETL stages, NAV dates will be converted to datetime format and reindexed across the full date range. Missing trading days caused by weekends and market holidays will be handled using forward-fill (`ffill()`).

---

# 7. AMFI Code Validation

Validation was performed between:

- Fund Master (`amfi_code`)
- NAV History (`amfi_code`)

## Validation Rule

Every AMFI code present in the Fund Master dataset must exist in the NAV History dataset.

## Result

**PASS**

All schemes present in the Fund Master dataset have corresponding NAV records available in the NAV History dataset.

No missing AMFI codes were identified.

---

# 8. Data Quality Assessment

| Check                  | Status |
| ---------------------- | ------ |
| Dataset Loading        | PASS   |
| Missing Value Review   | PASS   |
| Duplicate Check        | PASS   |
| Fund Master Validation | PASS   |
| AMFI Code Validation   | PASS   |
| NAV Validation         | PASS   |

---

# 9. Issues Identified

| Issue                                          | Severity | Action                       |
| ---------------------------------------------- | -------- | ---------------------------- |
| Missing `yoy_growth_pct` values in SIP dataset | Low      | Expected; no action required |
| No other quality issues detected               | None     | N/A                          |

---

# 10. Conclusion

All 10 datasets were successfully loaded and validated.

Key Findings:

- Total datasets analysed: 10
- Total records analysed: 87,533
- Total missing values: 12
- Total duplicate records: 0
- Total fund houses identified: 10
- Total categories identified: 2
- Total sub-categories identified: 12
- Total mutual fund schemes: 40

Data Quality Results:

- No duplicate records were detected.
- No critical missing values were identified.
- The only missing values were 12 observations in the SIP Year-over-Year Growth column, which is expected because prior-year comparison data is unavailable for the initial months.
- NAV History contains 46,000 complete records.
- Benchmark data contains 8,050 records.
- Investor transaction data contains 32,778 records.

AMFI Code Validation:

PASS

All 40 AMFI codes from the Fund Master dataset were found in the NAV History dataset. No missing scheme codes were detected.

Overall Assessment:

The datasets are of high quality and are ready for Day 2 activities including data cleaning, transformation, SQLite database design, and ETL implementation.
