-- Verify Row Counts

SELECT COUNT(*) AS nav_rows
FROM fact_nav;

SELECT COUNT(*) AS transaction_rows
FROM fact_transactions;

SELECT COUNT(*) AS fund_rows
FROM dim_fund;

SELECT COUNT(*) AS performance_rows
FROM fact_performance;

SELECT COUNT(*) AS aum_rows
FROM fact_aum;


-- Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV by Month

SELECT strftime('%Y-%m', nav_date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- SIP YoY Growth

SELECT *
FROM fact_sip_industry;

-- Transactions by State

SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1%

SELECT scheme_name
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- Average Transaction Amount

SELECT AVG(amount_inr)
FROM fact_transactions;

-- Funds by Risk Category

SELECT risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;

-- Top Fund Houses by Scheme Count

SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- Average Sharpe Ratio

SELECT AVG(sharpe_ratio)
FROM fact_performance;

-- Top Alpha Funds

SELECT amfi_code,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;
