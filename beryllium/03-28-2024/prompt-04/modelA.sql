SELECT i.name, SUM(s.quantity) AS quantity_sold, SUM(s.quantity * s.price) AS total_sales_value
FROM sales AS s
JOIN items AS i ON s.item_id = i.id
WHERE s.date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
GROUP BY i.name
ORDER BY quantity_sold DESC
LIMIT 3