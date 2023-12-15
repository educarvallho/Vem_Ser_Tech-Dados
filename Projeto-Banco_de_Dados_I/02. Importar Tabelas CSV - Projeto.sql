COPY ada.employees_clients (client_id, client_name) FROM 'D:\Employees_Clients.csv' DELIMITER ',' CSV HEADER;
COPY ada.employees_managers (manager_id, manager_name) FROM 'D:\Employees_Managers.csv' DELIMITER ',' CSV HEADER;
COPY ada.employees_states (state_id, state) FROM 'D:\Employees_States.csv' DELIMITER ',' CSV HEADER;
COPY ada.employment_types (employment_type_id, employment_type) FROM 'D:\Employment_Types.csv' DELIMITER ',' CSV HEADER;
COPY ada.employees_status (employee_id, first_name, last_name, state_id, employment_type_id, manager_id, employee_since, projects, salary, bonus) FROM 'D:\Employees_Status.csv' DELIMITER ',' CSV HEADER;
COPY ada.employees_sales (operation_id, employee_id, client_id, revenue, qty_sales) FROM 'D:\Employees_Sales.csv' DELIMITER ',' CSV HEADER;
