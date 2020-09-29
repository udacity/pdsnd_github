-- 4.Sometimes when people rent out movies they do not return them on time others do so return it before time.so as part of our reviews we want to know the total numbers of movies that were returned after the due date,before and on time
-- write a query that returns the number of movies that were returned before time, 
--  early and after the due date
/* Query */
WITH t1 AS (SELECT *, DATE_PART('day',return_date - rental_date) AS 
			date_difference,  RANK() OVER(PARTITION BY customer_id 
		   ORDER BY rental_id)AS Rank_number
			FROM rental rent),
t2 AS (SELECT rental_duration, date_difference,
	  CASE 
	  WHEN rental_duration > date_difference THEN 'Returned sooner'
	  WHEN rental_duration = date_difference THEN 'Returned after'
	  ELSE 'Returned late'
	   END AS Return_status
	   FROM film fi
	   JOIN inventory inv
	   USING (film_id)
	   JOIN t1
	   USING (inventory_id))
SELECT Return_status, count(*) AS total_no_films
      
FROM t2
GROUP BY 1
ORDER BY 2 DESC;



-- 3. we also want to know the category of movies people that people like.
--   So, write a query to find the most rented and rented type of movie or their genre and the total amount of sales made or the total amount of money made from those categories
-- /* Query 3 */
WITH t1 AS (SELECT cat.name AS Genre,
			COUNT (cus.customer_id) AS Total_rent_demand
           FROM category cat
		   JOIN film_category fc
		   USING(category_id)
		   JOIN film f 
		   USING(film_id)
		   JOIN inventory i
		   USING (film_id)
		   JOIN rental r
		   USING(inventory_id)
		   JOIN customer cus
		   USING(customer_id)
		   GROUP BY 1
		   ORDER BY 2 DESC),
t2 AS (SELECT cat.name AS Genre, SUM (py.amount) Sales_total
	       FROM category cat
	       JOIN film_category fc
	       USING(category_id)
	       JOIN film f
	  USING (film_id)
	  JOIN inventory i
	  USING(film_id)
	   JOIN rental rent 
	  USING (inventory_id)
	  JOIN payment py
	  USING (rental_id)
	  GROUP BY 1
	  ORDER BY 2 DESC)
SELECT t1.Genre, t1.Total_rent_demand,t2.Sales_total
FROM t1
JOIN t2
ON t1.Genre = t2.Genre;



-- 2.Here we want to know the movies that was release in particular years and also want to know the person who acted that movie and the other movies or genres the actor acted as well.
-- So, write a query that prints out the movie genres and the total number of movies made 

/* Query 2 */
WITH t1 AS(SELECT fi.title ,
              ac.first_name||' '||ac.last_name AS Actor_name,
              release_year , 
	c.name AS Genre,
       COUNT(ac.first_name||' '||ac.last_name) OVER (PARTITION BY 
													release_year )AS No_of_movie_made
FROM film fi
JOIN film_actor fa
ON fa.film_id = fi.film_id
JOIN film_category fc
ON fc.film_id = fi.film_id
JOIN category c
ON c.category_id = fc.category_id
JOIN actor ac
ON ac.actor_id = fa.actor_id
GROUP BY 1,2,3,4
ORDER BY Actor_name
Limit 10)
SELECT t1.genre,t1.No_of_movie_made
FROM t1

-- 1.we also want to review the performance of our staff; we want to know the total number of rentals they made in months and particularly which staff member did it.
-- Write a query that outputs the total number of rent our two staff members recorded in months

/*Query 1*/
WITH t1 AS (SELECT st.first_name||' '||st.last_name AS staff_full_name,
			st.staff_id,date_trunc('month', rent.rental_date) AS  rental_month
		    FROM staff st, rental rent)		
SELECT  
   staff_full_name,
    COUNT (rental_id)  AS rental_count
FROM t1
JOIN rental rent
ON rent.staff_id = t1.staff_id
JOIN staff st
ON st.staff_id = rent.staff_id
GROUP BY
    1
ORDER BY
    rental_count  desc



	 
			


