SELECT
    CONCAT(es.first_name, ' ', es.last_name) AS nome_completo,
    ROUND(es.salary + (es.salary * es.bonus), 2) AS salario_total,
    ROUND(SUM(eas.revenue), 2) AS receita_total,
    ROUND(SUM(eas.revenue) - (es.salary + (es.salary * es.bonus)), 2) AS diferenca
FROM
    ada.employees_status AS es
JOIN
    ada.employees_sales AS eas
ON
	es.employee_id = eas.employee_id
GROUP BY
    es.employee_id, nome_completo, salario_total
HAVING
    SUM(eas.revenue) < (es.salary + (es.salary * es.bonus))
ORDER BY
    diferenca;