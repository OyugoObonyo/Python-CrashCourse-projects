-- Get titles of all films starring Nick Wahlberg

SELECT title, actor.first_name, actor.last_name FROM film 
INNER join film_actor
ON film.film_id = film_actor.film_id
INNER JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'Nick' and actor.last_name = 'Wahlberg'