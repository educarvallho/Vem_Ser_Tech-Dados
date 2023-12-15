SELECT
    est.state,
    COUNT(*) AS numero_funcionarios
FROM
    ada.employees_status AS es
JOIN
    ada.employees_states AS est 
ON 
	es.state_id = est.state_id
GROUP BY
    est.state_id, est.state
ORDER BY
    numero_funcionarios DESC;