SELECT
    "Customer Name",
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY "Customer Name"
ORDER BY Revenue DESC
LIMIT 10;