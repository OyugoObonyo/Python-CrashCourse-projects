-- Get email address of customers living in california

SELECT district, customer.email FROM address
FULL OUTER JOIN customer
ON customer.address_id = address.address_id
WHERE district = 'California';