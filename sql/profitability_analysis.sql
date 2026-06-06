SELECT
    Category,
    ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY Category
ORDER BY Profit DESC;