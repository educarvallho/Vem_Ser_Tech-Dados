SELECT
    ec.client_name AS nome_cliente,
    MAX(es.revenue) AS receita_mais_alta,
    CONCAT(es2.first_name, ' ', es2.last_name) AS nome_funcionario
FROM
    ada.employees_sales AS es
JOIN
    ada.employees_clients AS ec
ON
	es.client_id = ec.client_id
JOIN
    ada.employees_status AS es2
ON
	es.employee_id = es2.employee_id
WHERE
    es.revenue = (
		SELECT MAX(revenue) 
		FROM ada.employees_sales)
GROUP BY
    nome_cliente,
	nome_funcionario;