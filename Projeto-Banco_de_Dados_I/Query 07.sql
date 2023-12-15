SELECT
    CONCAT(es.first_name, ' ', es.last_name) AS nome_completo,
    est.state AS estado,
    ROUND((es.salary + (es.salary * es.bonus)), 2) AS total_remuneracao,
    ROUND(
        (SELECT SUM((es2.salary + (es2.salary * es2.bonus)))
        FROM ada.employees_status AS es2
        WHERE est.state_id = es2.state_id), 2
    ) AS subtotal_estado
FROM
    ada.employees_status AS es
JOIN
    ada.employees_states AS est
ON
	es.state_id = est.state_id
WHERE
    est.state IN ('California', 'Texas', 'Florida')
ORDER BY
	estado,
	total_remuneracao DESC;