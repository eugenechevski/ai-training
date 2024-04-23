CREATE PARTITION FUNCTION pf_sales_date (datetime)
    AS RANGE RIGHT FOR VALUES ('2023-01-01', '2024-01-01', '2025-01-01');

CREATE PARTITION SCHEME ps_sales_date
    AS PARTITION pf_sales_date TO ([PRIMARY], [Sales2023], [Sales2024]); 

CREATE TABLE Sales 
(
    SaleID int,
    SaleDate datetime,
    CustomerID int,
    Amount decimal
) ON ps_sales_date(SaleDate);