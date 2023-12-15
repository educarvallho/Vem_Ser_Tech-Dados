SELECT
    CONCAT(first_name, ' ', last_name) AS nome_completo,
    employee_since AS data_ingresso,
    ROUND((CURRENT_DATE - employee_since) / 365) AS quantidade_anos
FROM
    ada.employees_status
ORDER BY
    data_ingresso DESC
LIMIT 1;