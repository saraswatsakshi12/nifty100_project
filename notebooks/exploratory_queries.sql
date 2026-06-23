-- Day 07 Exploratory Queries


-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;


-- 2. Company list
SELECT id, company_name
FROM companies
LIMIT 10;


-- 3. Profit and loss records
SELECT COUNT(*) AS pnl_records
FROM profitandloss;


-- 4. Balance sheet records
SELECT COUNT(*) AS balance_records
FROM balancesheet;


-- 5. Cashflow records
SELECT COUNT(*) AS cashflow_records
FROM cashflow;


-- 6. Top sales companies
SELECT company_id, sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;


-- 7. Highest profit companies
SELECT company_id, net_profit
FROM profitandloss
ORDER BY net_profit DESC
LIMIT 10;


-- 8. Average OPM
SELECT AVG(opm_percentage)
FROM profitandloss;


-- 9. Stock price count
SELECT COUNT(*) AS price_records
FROM stock_prices;


-- 10. Sector distribution
SELECT *
FROM sectors
LIMIT 10;