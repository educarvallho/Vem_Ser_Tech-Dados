SELECT
    CONCAT(es.first_name, ' ', es.last_name) AS nome_completo,
    ROUND(es.salary + (es.salary * es.bonus), 2) AS salario_total,
    et.employment_type AS tipo_jornada_trabalho
FROM
    ada.employees_status AS es
JOIN
    ada.employment_types AS et
ON
	es.employment_type_id = et.employment_type_id
WHERE
    (es.salary + (es.salary * es.bonus)) = (
        SELECT
            MAX(es2.salary + (es2.salary * es2.bonus))
        FROM
            ada.employees_status AS es2
        WHERE
            es2.employment_type_id = es.employment_type_id
    )
ORDER BY
    salario_total DESC;