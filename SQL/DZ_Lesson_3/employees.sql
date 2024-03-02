CREATE TABLE if NOT EXISTS employees(
"employee_id" INTEGER UNIQUE,
"departament_id" INTEGER,
"employee_name" TEXT NOT NULL,
"salary" INTEGER NOT NULL,
"hire_date" date);

/*
INSERT INTO employees (employee_id, departament_id, employee_name, salary, hire_date) VALUES
(1, 101, "John Doe", 50000, "2020-01-15"),
(2, 102, "Jane Smith", 60000, "2019-08-20"),
(3, 101, "Michael Johnson", 55000, "2021-03-10"),
(4, 103, "Emily Williams", 52000, "2018-11-05"),
(5, 102, "David Brown", 65000, "2017-06-30"),
(6, 103, "Jennifer Davis", 48000, "2020-09-25"),
(7, 101, "William Wilson", 70000, "2016-04-12"),
(8, 102, "Sarah Miller", 58000, "2019-01-08"),
(9, 103, "Kevin Martinez", 53000, "2017-10-22"),
(10, 101, "Laura Garcia", 51000, "2018-12-03");
*/

--1. Определить общее количество сотрудников в компании.
--SELECT count(*) FROM employees

--2. Рассчитать среднюю заработную плату в компании.
--SELECT avg(salary) FROM employees

--3. Определить количество сотрудников в каждом отделе.
--SELECT departament_id, count(*) FROM employees GROUP by departament_id

--5. Рассчитать общую сумму затрат на заработную плату для каждого отдела.
--SELECT departament_id, sum(salary) FROM employees GROUP by departament_id

--6. Найти средний стаж работы сотрудников в компании.
--SELECT avg(date() - hire_date) FROM employees

