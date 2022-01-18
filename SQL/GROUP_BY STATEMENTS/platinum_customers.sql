-- Customers found with 40 or more transactions offered platinum services

SELECT customer_id, COUNT(payment_id) from payment
group by customer_id
having COUNT(payment_id) >= 40