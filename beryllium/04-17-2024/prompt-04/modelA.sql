SELECT s.item_id, SUM(s.quantity) AS total_quantity
FROM sales AS s
WHERE DATE_TRUNC('month', s.sale_date) = DATE_TRUNC('month', NOW()) - INTERVAL '1 month'
GROUP BY s.item_id
ORDER BY total_quantity DESC
LIMIT 3