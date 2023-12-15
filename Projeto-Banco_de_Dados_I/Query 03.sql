SELECT
    est.state,
    SUM(eas.revenue) AS receita_total
FROM
    ada.employees_status AS es
JOIN
    ada.employees_states AS est
ON
	es.state_id = est.state_id
JOIN
    ada.employees_sales AS eas
ON
	es.employee_id = eas.employee_id
GROUP BY
    es.state_id, est.state
ORDER BY
    receita_total DESC
LIMIT 7;