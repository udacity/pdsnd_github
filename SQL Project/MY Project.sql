/*Query1 - the query used for the first insight*/
SELECT
   f.title AS Film_Name,
   COUNT(a.actor_id) AS Number_of_actors
FROM
   film_actor fa
   JOIN
      film f
      ON f.film_id = fa.film_id
   JOIN
      actor a
      ON a.actor_id = fa.actor_id
WHERE
   f.title = 'Chicago North'
GROUP BY
   f.title;

/*Query2 - the query used for the second insight*/
SELECT
   film_name AS film_name,
   number_of_actors AS number_of_actors
FROM
   (
      SELECT
         f.title AS film_name,
         COUNT(a.actor_id) AS number_of_actors
      FROM
         film_actor fa
         JOIN
            film f
            ON f.film_id = fa.film_id
         JOIN
            actor a
            ON a.actor_id = fa.actor_id
      GROUP BY
         f.title
   )
   sub
GROUP BY
   sub.film_name,
   sub.number_of_actors
ORDER BY
   number_of_actors DESC
LIMIT 10;

/*Query3 - the query used for the third insight*/
WITH t1 AS (
SELECT first_name||' '||last_name AS fullname,
       SUM(p.amount) AS total_amount
FROM customer c
JOIN payment p
ON c.customer_id = p.customer_id
GROUP BY 1
ORDER BY  2 DESC
LIMIT 5)

SELECT fullname,
       total_amount
FROM t1;


/*Query4 - the query used for the fourth insight*/
SELECT
   p.payment_date AS payment_date,
   CONCAT(first_name, ' ', last_name) AS customer_name,
   p.amount AS amount,
   AVG(P.amount) OVER (
ORDER BY
   p.payment_date) AS average_amount_of_payment
FROM
   payment p
   JOIN
      customer c
      ON p.customer_id = c.customer_id
   JOIN
      rental r
      ON p.rental_id = r.rental_id
   JOIN
      inventory i
      ON i.inventory_id = r.inventory_id
   JOIN
      film f
      ON f.film_id = i.inventory_id
WHERE
   f.title = 'Chicago North'
GROUP BY
   p.payment_date,
   c.first_name,
   c.last_name,
   p.amount
having
   MIN(amount) > 0.00;
