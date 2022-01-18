-- Films that have truman anywhere in the title

SELECT COUNT(*) FROM film
WHERE title
LIKE '%Truman%';