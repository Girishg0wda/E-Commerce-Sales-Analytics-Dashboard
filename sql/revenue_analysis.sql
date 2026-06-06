SELECT
    Region,
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY Region
ORDER BY Revenue DESC;