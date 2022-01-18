-- Select film with R ratings and a replacement cost btwn 5 & 15

SELECT COUNT(*) FROM film
WHERE rating = 'R'
AND replacement_cost 
BETWEEN 5.00 AND 15.00;