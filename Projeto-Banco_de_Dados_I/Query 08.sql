SELECT
    CONCAT(es.first_name, ' ', es.last_name) AS nome_completo,
    est.state AS estado,
    ROUND((es.salary * es.bonus), 2) AS bonus_total
FROM
    ada.employees_status AS es
JOIN
    ada.employees_states AS est
ON
	es.state_id = est.state_id
WHERE
    est.state IN ('California', 'Texas', 'Florida')
    AND (es.salary * es.bonus) > 3000
ORDER BY
    bonus_total DESC;