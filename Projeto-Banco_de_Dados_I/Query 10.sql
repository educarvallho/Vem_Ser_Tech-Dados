SELECT
    CONCAT(es.first_name, ' ', es.last_name) AS nome_completo,
    eas.qty_sales AS quantidade_vendas,
    eas.revenue AS receita
FROM
    ada.employees_status AS es
JOIN
    ada.employees_sales AS eas
ON
	es.employee_id = eas.employee_id
ORDER BY
    quantidade_vendas DESC,
	receita DESC
LIMIT 1;