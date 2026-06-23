-- Day 06 Manual Review


-- 1. Total companies

SELECT 
COUNT(*) AS total_companies
FROM companies;



-- 2. Random 5 companies

SELECT *
FROM companies
ORDER BY RANDOM()
LIMIT 5;



-- 3. Year coverage

SELECT
company_id,
COUNT(DISTINCT year) AS years_available

FROM profitandloss

GROUP BY company_id

ORDER BY years_available;



-- 4. Companies having less than 5 years

SELECT

company_id,
COUNT(DISTINCT year) AS years

FROM profitandloss

GROUP BY company_id

HAVING years < 5;



-- 5. Missing financial data

SELECT

c.company_name,
p.year,
p.sales,
p.net_profit

FROM companies c

LEFT JOIN profitandloss p

ON c.id = p.company_id

WHERE p.company_id IS NULL;


-- 6. Check negative sales

SELECT *

FROM profitandloss

WHERE sales < 0;