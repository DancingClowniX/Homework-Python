CREATE TABLE if not EXISTS Restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    phone TEXT,
    number_desk INTEGER
);

CREATE TABLE if not EXISTS Desk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    desk_number INTEGER,
    capacity INTEGER,
    reservation TEXT,
    restaurant_id INTEGER,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id)
);

CREATE TABLE if not EXISTS Reservation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    desk_number INTEGER,
    reservation_time TEXT,
    desk_Id INTEGER,
    FOREIGN KEY (desk_id) REFERENCES Desk(id)
);

CREATE TABLE if not EXISTS Waiters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
	id_restaurant INTEGER,
	FOREIGN KEY (id_restaurant) REFERENCES Restaurant(id)
);
/*
INSERT INTO Restaurant (name, address, phone, number_desk) VALUES 
('Restaurant A', '123 Main St', '555-1234', 10),
('Restaurant B', '456 Elm St', '555-5678', 8),
('Restaurant C', '789 Oak St', '555-9090', 12),
('Restaurant D', '321 Maple St', '555-4321', 15),
('Restaurant E', '654 Pine St', '555-8765', 20),
('Restaurant F', '987 Birch St', '555-3456', 5),
('Restaurant G', '159 Cedar St', '555-6789', 10),
('Restaurant H', '753 Walnut St', '555-3456', 8),
('Restaurant I', '852 Spruce St', '555-1234', 6),
('Restaurant J', '951 Sycamore St', '555-5678', 10);

INSERT INTO Desk (desk_number, capacity, reservation, restaurant_id) VALUES 
(1, 4, 'Yes', 1),
(2, 6, 'No', 1),
(3, 2, 'Yes', 2),
(4, 8, 'No', 2),
(5, 5, 'Yes', 3),
(6, 3, 'No', 3),
(7, 4, 'Yes', 4),
(8, 7, 'No', 4),
(9, 6, 'Yes', 5),
(10, 10, 'No', 5);

INSERT INTO Reservation (client_name, desk_number, reservation_time, desk_Id) VALUES 
('John Doe', 1, '2022-07-15 19:00:00', 1),
('Jane Smith', 3, '2022-07-20 20:00:00', 3),
('Mike Johnson', 5, '2022-07-25 18:30:00', 5),
('Sarah Davis', 7, '2022-08-01 17:00:00', 7),
('Robert Brown', 9, '2022-08-05 18:45:00', 9),
('Emily White', 2, '2022-08-10 19:30:00', 2),
('David Wilson', 4, '2022-08-15 20:15:00', 4),
('Jennifer Lee', 6, '2022-08-20 18:00:00', 6),
('Daniel Perez', 8, '2022-08-25 17:45:00', 8),
('Maria Garcia', 10, '2022-08-30 19:15:00', 10);

INSERT INTO Waiters (name,id_restaurant) VALUES 
('Alice',1),
('Bob',1),
('Charlie',2),
('Diane',2),
('Eve',3),
('Frank',3),
('Gina',4),
('Harry',4),
('Irene',5),
('Jack',5),
('Carl',6),
('Sofi',6),
('Clay',7),
('Whinston',7),
('Lana',8),
('Tom',8),
('Hesus',9),
('Ron',9),
('Kurt',10),
('Perl',10);
*/

--1. Запрос на получение информации о ресторане:
--Получить название, адрес и контактный телефон ресторана с идентификатором 1.
--SELECT * FROM Restaurant where id = 1

--2. Запрос на выборку доступных столов:
--Получить номера и вместимость столов, доступных для бронирования в ресторане с идентификатором 2.
--SELECT * FROM Desk
--JOIN Restaurant on Restaurant.id = Desk.restaurant_id
--WHERE Restaurant.id = 2


--3. Запрос на получение списка бронирований для ресторана:
--Получить информацию о бронированиях, включая идентификатор бронирования,
--имя клиента, номер столика и время бронирования для столов из ресторана с идентификатором 3.
--SELECT * FROM Restaurant
--JOIN Desk on Desk.restaurant_id = Restaurant.id
--JOIN Reservation on Desk.id = Reservation.desk_Id
--where Restaurant.id = 3



--4. Запрос на получение списка официантов для ресторана:
--Получить идентификатор и имя официантов, работающих в ресторане с идентификатором 4.
--SELECT * FROM Restaurant
--JOIN Waiters on Restaurant.id = Waiters.id_restaurant
--where Restaurant.id = 4

--7. Запрос на получение информации о бронировании по идентификатору:
--Получить все данные о бронировании с идентификатором 7.
--SELECT * FROM Reservation


--8. Запрос на подсчет количества столов в ресторане:
--Получить общее количество столов в ресторане с идентификатором 8.
--SELECT name,number_desk FROM Restaurant
--WHERE Restaurant.id = 8

--9. Запрос на выборку столов по вместимости:
--Получить номера и вместимость столов, вместимость которых больше или равна 6.
--SELECT name, number_desk,desk_number FROM Restaurant
--JOIN Desk on Desk.restaurant_id = Restaurant.id
--WHERE capacity >=6;

--10. Запрос на поиск информации о клиенте по имени:
--Найти всех клиентов, имя которых содержит "John".
--SELECT * FROM Reservation
--WHERE client_name like "John%"