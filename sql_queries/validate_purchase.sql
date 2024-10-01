-- 1. Validate the Order Exists in the 'orders' table
SELECT o.order_id, o.customer_id, o.order_date, o.total_amount, o.order_status
FROM orders o
WHERE o.order_id = 1;  -- Replace with the actual order_id

-- Expected Output:
-- +----------+-------------+---------------------+--------------+--------------+
-- | order_id | customer_id  | order_date          | total_amount | order_status |
-- +----------+-------------+---------------------+--------------+--------------+
-- |        1 |         123  | 2024-09-30 14:22:01 |         99.99| CONFIRMED    |
-- +----------+-------------+---------------------+--------------+--------------+


-- 2. Validate that the correct products were purchased
SELECT oi.product_id, p.product_name, oi.quantity, oi.unit_price, oi.total_price
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 1;  -- Replace with the actual order_id

-- Expected Output:
-- +------------+-----------------------+----------+------------+-------------+
-- | product_id | product_name           | quantity | unit_price | total_price |
-- +------------+-----------------------+----------+------------+-------------+
-- |          1 | Sauce Labs Backpack    |        1 |      29.99 |       29.99 |
-- |          2 | Sauce Labs Bike Light  |        2 |       9.99 |       19.98 |
-- +------------+-----------------------+----------+------------+-------------+


-- 3. Verify that product stock has been reduced accordingly in the 'products' table
SELECT product_id, product_name, stock_quantity
FROM products
WHERE product_id IN (1, 2);  -- Replace with actual product IDs

-- Expected Output:
-- +------------+-----------------------+----------------+
-- | product_id | product_name           | stock_quantity  |
-- +------------+-----------------------+----------------+
-- |          1 | Sauce Labs Backpack    |             99 |  -- Stock reduced by 1
-- |          2 | Sauce Labs Bike Light  |             48 |  --
