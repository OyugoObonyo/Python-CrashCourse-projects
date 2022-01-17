-- Customer IDs of 1st 10 paying customers

SELECT customer_id FROM payment
WHERE amount != 0.0
ORDER BY payment_date ASC
LIMIT 10;