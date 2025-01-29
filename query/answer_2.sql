-- Total Dollars Used = sum of the total dollars used on the day
SELECT 
    DISTINCT submit_date,
    sum( dollars_used ) over ( partition BY submit_date ) AS Dollar_Used
FROM applications
ORDER BY submit_date ASC;
-- Total Approved Dollars = sum of the total approved dollars on the day
SELECT 
    DISTINCT submit_date,
    sum( approved_amount ) over ( partition BY submit_date ) AS Dollar_Approved
FROM applications
WHERE approved = TRUE
ORDER BY submit_date ASC;
-- Total Applications = number of applications submitted on the day
SELECT 
    DISTINCT submit_date,
    count(application_id) 
    over( PARTITION BY submit_date ) AS "Total Applications"
FROM applications ;
-- Total Approved Applications= number of approved applications on the day
SELECT 
    DISTINCT submit_date,
    count(application_id) 
    over( PARTITION BY submit_date ) AS "Approved Applications"
FROM applications 
WHERE approved = TRUE;
-- Total Campaigns = Number of campaigns that contributed to the day’s applications
SELECT
    DISTINCT a.submit_date, 
    count(c.campaign)
    over (PARTITION BY submit_date)
    AS "number of campaigns"
FROM 
    applications AS a 
    JOIN customers AS c
    ON a.customer_id = c.customer_id
WHERE c.campaign <> 0;
-- Running Total of Applications = shows the total number of applications submitted by the store on the day
SELECT 
    DISTINCT store,
    submit_date,
    count (application_id) 
    over (PARTITION BY submit_date ) AS "Running Total of Applications"
FROM applications
WHERE store = "store_32";
-- The rolling 30-day average of dollars used = The average of the last 30 days.
WITH max_date_cte AS (
    SELECT  max(submit_date) AS max_date
    FROM applications
    )
SELECT avg(dollars_used) AS avg_dol_used
FROM applications
WHERE
    submit_date BETWEEN
    (SELECT DATE(max_date, '-30 days') FROM max_date_cte )
    AND (SELECT max_date FROM max_date_cte);
