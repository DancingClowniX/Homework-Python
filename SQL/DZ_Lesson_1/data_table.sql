---------------------------------- Задача 1-------------------------------------------------
/*
CREATE TABLE group_s(
name TEXT NOT NULL,
rate INTEGER NOT NULL,
course INTEGER not null)

INSERT INTO "main"."group_s" ("name", "rate", "course") VALUES ('Phylosophy', '3', '5429');
INSERT INTO "main"."group_s" ("name", "rate", "course") VALUES ('Mathematics', '1', '2345');
INSERT INTO "main"."group_s" ("name", "rate", "course") VALUES ('Geografics', '2', '3321');
INSERT INTO "main"."group_s" ("name", "rate", "course") VALUES ('Django', '50', '4429');

--SELECT * FROM group_s WHERE rate = 50;--

---------------------------------- Задача 2-------------------------------------------------
*/
/*CREATE TABLE IF NOT EXISTS weapons(
"name" TEXT NOT NULL,
"type" TEXT NOT NULL,
"power" INTEGER NOT NULL
);
*/


/*
INSERT INTO weapons ("name","type","power") VALUES("knife","cold",200);
insert INTO weapons ("name","type","power") VALUES("glock17","firearms",80);
INSERT INTO weapons ("name","type","power") VALUES("shotgun","firearms",160);
*/

/*
SELECT * FROM weapons
*/
--SELECT * FROM weapons WHERE power >= 200;

---------------------------------- Задача 3-------------------------------------------------
/*
CREATE TABLE games(
name TEXT NOT NULL,
data date INTEGER NOT NULL,
time_save time INTEGER not null)
*/

/*
INSERT INTO games ("name","data","time_save") VALUES("tetris", "2024-08-20", "18:23:00");
INSERT INTO games ("name","data","time_save") VALUES("counter_strike", "2023-10-07", "11:03:56");
INSERT INTO games ("name","data","time_save") VALUES("Minecraft", "2024-03-11", "06:54:23");
*/

SELECT * FROM games