
/* ---------- Query 1 - Number of rentals of top 10 renting countries ---------- */

WITH t1 AS (SELECT c3.customer_id, 
                   p.rental_id
              FROM country AS c1
                   JOIN city AS c2
                    ON c1.country_id = c2.country_id
                   JOIN address a
                    ON c2.city_id = a.city_id
                   JOIN customer c3
                    ON a.address_id = c3.address_id
                   JOIN payment p
                    ON c3.customer_id = p.customer_id
                   JOIN (
                        SELECT c1.country_id
                          FROM country AS c1
                               JOIN city AS c2
                                ON c1.country_id = c2.country_id
                               JOIN address a
                                ON c2.city_id = a.city_id
                               JOIN customer c3
                                ON a.address_id = c3.address_id
                               JOIN payment p
                                ON c3.customer_id = p.customer_id
                         GROUP BY 1
                         ORDER BY SUM(p.amount) DESC
                         LIMIT 10) sub
                 ON sub.country_id = c1.country_id),
					
     t2 AS (SELECT c.name,
                   COUNT(r.rental_id) AS count_top10
              FROM t1
                   JOIN rental AS r
                    ON r.rental_id = t1.rental_id
                   JOIN inventory AS i
                    ON i.inventory_id = r.inventory_id
                   JOIN film f
                    ON f.film_id = i.film_id
                   JOIN film_category fc
                    ON f.film_id = fc.film_id
                   JOIN category c
                    ON c.category_id = fc.category_id
             GROUP BY 1),

     t3 AS (SELECT c.name,
                   COUNT(r.rental_id) AS rental_count
              FROM rental AS r
                   JOIN inventory AS i
                    ON i.inventory_id = r.inventory_id
                   JOIN film f
                    ON f.film_id = i.film_id
                   JOIN film_category fc
                    ON f.film_id = fc.film_id
                   JOIN category c
                    ON c.category_id = fc.category_id
             GROUP BY 1)
		
SELECT t2.name AS category,
       t3.rental_count - t2.count_top10 AS other_countries,
       t2.count_top10,
       CAST(t2.count_top10*100 AS FLOAT)/t3.rental_count AS "proportion(%)"
  FROM t2
       JOIN t3
        ON t2.name = t3.name
 ORDER BY 2 DESC;
