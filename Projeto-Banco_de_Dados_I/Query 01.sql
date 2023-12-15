SELECT
    et.employment_type AS tipo_jornada_trabalho,
    ROUND(AVG(es.salary + (es.salary * es.bonus)), 2) AS media_salario
FROM
    ada.employees_status AS es
JOIN
    ada.employment_types AS et
ON 
    es.employment_type_id = et.employment_type_id
GROUP BY
    et.employment_type
ORDER BY
    media_salario DESC;