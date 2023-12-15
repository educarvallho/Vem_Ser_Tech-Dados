-- Criar um schema ada
CREATE SCHEMA ada

CREATE TABLE ada.employees_clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(50) NOT NULL
);

CREATE TABLE ada.employees_managers (
    manager_id SERIAL PRIMARY KEY,
    manager_name VARCHAR(50) NOT NULL
);

CREATE TABLE ada.employees_states (
    state_id SERIAL PRIMARY KEY,
    state VARCHAR(50) NOT NULL
);

CREATE TABLE ada.employment_types (
    employment_type_id SERIAL PRIMARY KEY,
    employment_type VARCHAR(50) NOT NULL
);

CREATE TABLE ada.employees_status (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    state_id INTEGER,
    employment_type_id INTEGER,
    manager_id INTEGER,
    employee_since DATE,
    projects INTEGER,
    salary DECIMAL(10, 2),
    bonus DECIMAL(5, 2),
    FOREIGN KEY (state_id) REFERENCES ada.employees_states(state_id),
    FOREIGN KEY (employment_type_id) REFERENCES ada.employment_types(employment_type_id),
    FOREIGN KEY (manager_id) REFERENCES ada.employees_managers(manager_id)
);

CREATE TABLE ada.employees_sales (
    operation_id SERIAL PRIMARY KEY,
    employee_id INTEGER,
    client_id INTEGER,
    revenue DECIMAL(10, 2),
    qty_sales INTEGER,
    FOREIGN KEY (employee_id) REFERENCES ada.employees_status(employee_id),
	FOREIGN KEY (client_id) REFERENCES ada.employees_clients(client_id)
);
