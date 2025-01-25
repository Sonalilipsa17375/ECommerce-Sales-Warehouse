-- Total sales by category
SELECT c.categories, SUM(p.price * cart.quantity) AS total_revenue
FROM Carts cart
JOIN Products p ON cart.productId = p.ProductsId
JOIN Categories c ON p.CategoryId = c.CategoryId
GROUP BY c.categories;

-- Top-selling products
SELECT p.title, SUM(cart.quantity) AS total_sold
FROM Carts cart
JOIN Products p ON cart.productId = p.ProductsId
GROUP BY p.title
ORDER BY total_sold DESC
LIMIT 10;

-- Sales trends over time
SELECT DATE_TRUNC('month', cart.date) AS sales_month, SUM(p.price * cart.quantity) AS total_revenue
FROM Carts cart
JOIN Products p ON cart.productId = p.ProductsId
GROUP BY sales_month
ORDER BY sales_month;
