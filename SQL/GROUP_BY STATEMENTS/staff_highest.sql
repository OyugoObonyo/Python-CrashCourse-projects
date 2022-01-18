-- Staff who handles the most amount of processed payments

SELECT staff_id, COUNT(payment_id) FROM payment
GROUP BY staff_id