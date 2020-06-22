/* ---------- Query 2 - Film rentals distribution by category ---------- */

SELECT f.title,
       c.name,
       COUNT(r.rental_id) AS rental_count,
       NTILE(4) OVER (PARTITION BY c.name ORDER BY COUNT(r.rental_id))
  FROM category AS c
       JOIN film_category AS fc
        ON c.category_id = fc.category_id
       JOIN film AS f
        ON f.film_id = fc.film_id
       JOIN inventory AS i
        ON f.film_id = i.film_id
       JOIN rental AS r
        ON i.inventory_id = r.inventory_id
 GROUP BY 1, 2
 ORDER BY 2 DESC, 4;
