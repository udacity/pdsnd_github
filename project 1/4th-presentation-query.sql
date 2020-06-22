/* ---------- Query 4 - Film rental distribution by category ---------- */

WITH t1 AS (SELECT c.customer_id, 
                   p.amount, 
                   DATE_TRUNC('month', p.payment_date) AS payment_date,
			         p.rental_id
              FROM customer AS c
                   JOIN payment AS p
                    ON c.customer_id = p.customer_id),

     t2 AS (SELECT t1.customer_id, 
		   t1.payment_date,
                   SUM(t1.amount) AS total_amtpaid,
                   LEAD(SUM(t1.amount)) OVER(w) AS lead_num,
                   LEAD(SUM(t1.amount)) OVER(w) - SUM(t1.amount) AS lead_dif,
                   CASE 
                       WHEN LEAD(SUM(t1.amount)) OVER(w) - SUM(t1.amount) < 0 THEN 0
                       WHEN LEAD(SUM(t1.amount)) OVER(w) - SUM(t1.amount) >= 0 THEN 1
                   END AS progress
              FROM t1
                   JOIN rental AS r
                    ON r.rental_id = t1.rental_id
                    AND t1.customer_id = r.customer_id
             GROUP BY 1, 2
            WINDOW w AS (PARTITION BY t1.customer_id ORDER BY DATE_TRUNC('month', t1.payment_date)))
										  
SELECT t2.payment_date,
       COUNT(*) AS total_count,
       SUM(t2.progress) AS progress_bymon,
       COUNT(*) - SUM(t2.progress) AS regress_bymon
  FROM t2
 WHERE t2.progress IS NOT NULL
 GROUP BY 1
 ORDER BY 1;
