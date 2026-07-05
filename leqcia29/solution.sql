CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO departments (id, name, location) VALUES
(1, 'IT', 'New York'),
(2, 'Marketing', 'Los Angeles'),
(3, 'Finance', 'Chicago'),
(4, 'HR', 'New York');

INSERT INTO employees (id, name, salary, department_id) VALUES
(1, 'Giorgi', 3500.00, 1),
(2, 'Nino', 4200.00, 1),
(3, 'Luka', 2800.00, 2),
(4, 'Mariam', 3000.00, 2),
(5, 'Ana', 5000.00, 3),
(6, 'Dato', 2600.00, 4);

SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

SELECT
    name,
    salary,
    (
        SELECT departments.name
        FROM departments
        WHERE departments.id = employees.department_id
    ) AS department_name
FROM employees;

SELECT *
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'New York'
);

SELECT *
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.id
);

SELECT *
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department_id = (
        SELECT id
        FROM departments
        WHERE name = 'Marketing'
    )
);

SELECT *
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department_id = (
        SELECT id
        FROM departments
        WHERE name = 'IT'
    )
);

SELECT *
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'New York'
)
UNION
SELECT *
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'Los Angeles'
);

SELECT *
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'New York'
)
UNION ALL
SELECT *
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'Los Angeles'
);
