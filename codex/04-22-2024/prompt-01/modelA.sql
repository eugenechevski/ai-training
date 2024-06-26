
CREATE TABLE orders
(
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE
(order_date)
(
  PARTITION p2023_01 VALUES LESS THAN
('2023-02-01'),
  PARTITION p2023_02 VALUES LESS THAN
('2023-03-01'),
  ...
  PARTITION p2024_01 VALUES LESS THAN
('2024-02-01')
);