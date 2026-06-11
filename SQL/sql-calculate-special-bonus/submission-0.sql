-- Write your query below
select employee_id , 
        CASE
            WHEN 
                employee_id % 2 != 0 and
                name not like 'M%'
            THEN 
                salary
            ELSE 0
        END as Bonus

    from employees
    ORDER BY employee_id;