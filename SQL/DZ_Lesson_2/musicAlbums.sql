CREATE TABLE IF NOT EXISTS albums(
"id" INTEGER PRIMARY KEY AUTOINCREMENT,
"title" TEXT NOT NULL,
"artist" TEXT NOT NULL,
"realase_date" date,
"genre" TEXT NOT NULL);

/*
INSERT INTO albums ("title","artist","realase_date","genre")
VALUES
("Astroworld","Travis Scott","2018-01-01","hip-hop"),
("Mr.Hood","KMD","1991-01-01","hip-hop"),
("Lemonade","Beyonce","2016-01-01","rock"),
("Red","Taylor Swift","2012-01-01","rock"),
("Stg.Pepper`s Lonely Herts Club Band","The beatles","1967-01-01","rock"),
("Rovolver","The beatles","1966-01-01","rock"),
("Off the Wall","Michael Jackson","1979-01-01","pop"),
("Graceland","Paul Simon","1986-01-01","hip-hop"),
("Superfly","Curtis Mayfield","1972-01-01","Soundtrack"),
("Stand!","Sly and the Family Stone","1969-01-01","R&B / Soul"),
("Blackout","Britney Spears","2007-01-01","pop")
*/

--●	Получить список всех альбомов вместе с их названиями, исполнителями, датами выпуска и жанрами.
--SELECT * FROM albums

--●	Найти альбомы, выпущенные после 2015 года.
--SELECT * FROM albums WHERE realase_date>"2015-01-01"

--●	Получить список альбомов жанра "Рок".
--SELECT * FROM albums WHERE genre like "rock"

--●	Найти альбомы с названием, начинающимся на букву "S".
--SELECT * FROM albums WHERE title like "S%"

--●	Получить список альбомов, исполнителями которых являются "The Beatles".
--SELECT * FROM albums WHERE artist like "The beatles"

--●	Найти альбомы жанра "Хип-хоп", выпущенные до 2010 года.
--SELECT * FROM albums WHERE genre like "hip-hop" AND realase_date<"2010-01-01"

--●	Найти альбомы с датой выпуска после 2000 года и жанром "Поп".
--SELECT * FROM albums WHERE genre like "pop" AND realase_date>"2000-01-01"