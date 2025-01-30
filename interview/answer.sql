-- You have two tables: 'employees' and 'sales'. 
-- The 'employees' table contains employee details, and the 'sales' table contains sales transactions made by employees.

-- **employees table**
-- employee_id | first_name | last_name | department_id
-- ----------------------------------------------------
-- 1           | John       | Doe       | 1
-- 2           | Jane       | Smith     | 1
-- 3           | Robert     | Brown     | 2
-- 4           | Alice      | White     | 2

-- **sales table**
-- sale_id | employee_id | sale_amount | sale_date
-- ---------------------------------------------
-- 1       | 1          | 1000        | 2021-01-01
-- 2       | 1          | 1500        | 2021-02-01
-- 3       | 2          | 2000        | 2021-01-05
-- 4       | 2          | 2500        | 2021-03-01
-- 5       | 3          | 1200        | 2021-01-01
-- 6       | 3          | 1800        | 2021-02-15
-- 7       | 4          | 1700        | 2021-02-10
-- 8       | 4          | 2200        | 2021-03-10

-- **Task:**
-- Write a SQL query to calculate the **total sales** and **average sales amount** per department, 
-- but only for the employees who made more than one sale. 
-- For employees who made multiple sales, also include the **rank of the employee** in their department based on their total sales amount, 
-- where rank 1 is given to the employee with the highest sales in that department.

WITH employee_sales AS (
    -- Step 1: Filter employees with more than one sale and calculate their total and average sales
    SELECT 
        s.employee_id,
        COUNT(s.sale_id) AS num_sales,
        SUM(s.sale_amount) AS total_sales,
        AVG(s.sale_amount) AS avg_sales
    FROM 
        sales s
    GROUP BY 
        s.employee_id
    HAVING 
        COUNT(s.sale_id) > 1
),
department_sales AS (
    -- Step 2: Join with employees table to get department info and calculate department-level aggregates
    SELECT 
        e.department_id,
        es.employee_id,
        es.total_sales,
        es.avg_sales,
        SUM(es.total_sales) OVER (PARTITION BY e.department_id) AS department_total_sales,
        AVG(es.avg_sales) OVER (PARTITION BY e.department_id) AS department_avg_sales
    FROM 
        employee_sales es
    JOIN 
        employees e ON es.employee_id = e.employee_id
),
ranked_employees AS (
    -- Step 3: Rank employees within their department based on total sales
    SELECT 
        ds.department_id,
        ds.employee_id,
        ds.total_sales,
        ds.avg_sales,
        ds.department_total_sales,
        ds.department_avg_sales,
        RANK() OVER (PARTITION BY ds.department_id ORDER BY ds.total_sales DESC) AS sales_rank
    FROM 
        department_sales ds
)
-- Final Step: Select the required columns
SELECT 
    department_id,
    department_total_sales AS total_sales_per_department,
    department_avg_sales AS avg_sales_per_department,
    employee_id,
    total_sales AS employee_total_sales,
    avg_sales AS employee_avg_sales,
    sales_rank
FROM 
    ranked_employees
ORDER BY 
    department_id, sales_rank;