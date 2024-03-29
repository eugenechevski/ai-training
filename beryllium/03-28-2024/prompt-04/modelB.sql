SELECT item_name, COUNT(*) AS quantity_sold, SUM(sales_price) AS total_sales_value
FROM sales
JOIN items ON items.item_id = sales.item_id
WHERE sale_date BETWEEN '2023-01-01' AND '2023-01-31'
GROUP BY item_name
ORDER BY quantity_sold DESC, total_sales_value DESC
LIMIT 3;