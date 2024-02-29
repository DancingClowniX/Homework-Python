CREATE TABLE IF NOT EXISTS films(
"id" INTEGER PRIMARY KEY AUTOINCREMENT,
"title" TEXT NOT NULL,
"realase_date" date,
"genre" TEXT,
"duration" INT);
/*
INSERT INTO films (title,realase_date,genre,duration)
VALUES ("Закон и порядок","2024-01-23","Comedy",120)

INSERT INTO films (title,realase_date,genre,duration)
VALUES ("Вошка-басурманка","2009-07-15","Fantastic",177)

INSERT INTO films (title,realase_date,genre,duration)
VALUES ("Бабуин-красавец","2011-04-28","Action",160);

INSERT INTO films (title,realase_date,genre,duration)
VALUES ("Моя девушка Сара","2004-05-21","Action",140);

INSERT INTO films (title,realase_date,genre,duration)
VALUES ("Седьмое небо","2015-10-19","Horror",99)
*/

--●	Получить список всех фильмов вместе с их названиями, датами выхода и жанрами.
--SELECT * FROM films

--●	Найти фильмы, вышедшие после 2010 года.
--SELECT * FROM films WHERE realase_date>"2005-01-01"

--●	Получить список фильмов жанра "Фантастика".
--SELECT * FROM films WHERE "genre" like "Fantastic";

--●	Найти фильмы с длительностью более 150 минут.
--SELECT * FROM films WHERE "duration" >150

--●	Получить список фильмов, названия которых начинаются на букву "В".
--SELECT * FROM films WHERE title like "В%"

--●	Найти фильмы жанра "Боевик", вышедшие до 2005 года.
--SELECT * FROM films WHERE genre like "Action" AND realase_date <"2005-01-01"

--●	Найти фильмы с длительностью менее 120 минут.
--SELECT * FROM films WHERE duration <120