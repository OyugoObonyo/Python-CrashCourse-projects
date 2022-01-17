-- Returns all active customers i.e their first and last name

SELECT first_name, last_name FROM customer WHERE activebool = 'True';