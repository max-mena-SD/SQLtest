
 -- Create a table to determine, for each store, the customer who has spent the highest 
 -- total amount (dollars_used) through their approved applications. Include the store name, 
 -- customer ID, customer's first and last name, dollars used.
CREATE TABLE customer_spent_highest AS
    WITH test AS ( 
    SELECT
        s.store,
        c.customer_id,
        c.first_name,
        c.last_name,
        sum(a.dollars_used) 
        over(PARTITION BY customer_id) AS spend
        
    FROM stores AS s
        JOIN applications AS a USING ( store )
        JOIN customers AS c USING (customer_id)
    GROUP BY
        s.store,
        c.customer_id )
    SELECT store, customer_id, first_name, last_name, max(spend) AS max_spend
    FROM test
    GROUP BY store
    ORDER BY max_spend DESC;

