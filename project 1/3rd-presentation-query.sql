/* ---------- Query 3 - Amount spent by the top 10 paying customers between February and April 2007 ---------- */

WITH t1 AS (SELECT (first_name || ' ' || last_name) AS name, 
                   c.customer_id, 
                   p.amount, 
                   p.payment_date
              FROM customer AS c
                   JOIN payment AS p
                    ON c.customer_id = p.customer_id),

     t2 AS (SELECT t1.customer_id
              FROM t1
             GROUP BY 1
             ORDER BY SUM(t1.amount) DESC
             LIMIT 10),

     t3 AS (SELECT t1.name,
                   DATE_TRUNC('month', t1.payment_date) AS pay_mon, 
                   COUNT(*) AS pay_countpermon,
                   SUM(t1.amount) AS pay_amount
              FROM t1
                   JOIN t2
                    ON t1.customer_id = t2.customer_id
              WHERE t1.payment_date BETWEEN '20070101' AND '20080101'
              GROUP BY 1, 2
              ORDER BY 1, 3, 2)

SELECT t3.name,
       t3.pay_mon,
       t3.pay_amount,
	    ROUND(AVG(t3.pay_amount) OVER (PARTITION BY t3.name), 2) AS avg_amount					
  FROM t3
 ORDER BY 1, 2;
