INSERT INTO genre
VALUES
    (1,'Поп-музыка'), 
    (2,'Рок'), 
    (3,'Хип-Хоп'), 
    (4,'Electronic'), 
    (5,'Классика');
insert into musician
values 
(21,'Linkin Park'),
(22,'Rammstein'),
(31,'Eminem'),
(32,'Kanye West'),
(51,'Ludwig v. Beethoven'),
(52,'Pyotr Chaikovskiy'),
(41,'Daft Punk'), 
(11,'JONY');

insert into album
values (100,'Албом Daft Punk', 1978),
(101,'Альбом Emninem_1', 2005), 
(102,'Альбом Rammstein', 1991),
(103,'Альбом Eminem_2', 2019),
(104,'Альбом Linkin Park', 2004), 
(105,'Альбом JONY', 2010), 
(106,'Альбом Kanye West', 2003),
(107,'Альбом Beethoven', 1901),
(108,'Альбом Chaikovkiy', 1920);

insert into track(album_id, name, duration) 
values
(102, 'Mann gegen Mann', 231), 
(108, 'Вальс', 106), 
(101, 'Rap God', 213), 
(105, 'Никак', 350), 
(103, 'Venom', 269),
(104, 'My Fall', 262), 
(106, 'Graduation Day', 82),
(106,'Jesus Walks', 193), 
(104, 'Faint', 162), 
(104, 'Numb', 188),
(103, 'If I Had', 244),
(103, 'Brain Damage', 226),
(101, 'Never 2 Far', 218),
(100, 'Robot Rock', 388), 
(107, 'Симфония № 5 1-я часть', 420);

insert into collection
values (1, 'Favourite', 2015),
(2, 'The Best', 2018), 
(3, 'New', 2020), 
(4, 'Fun', 2017), 
(5, 'Awesome', 2021), 
(6, 'Cool', 2014), 
(7, 'Big', 2019),
(8, 'Finally', 2013);

insert into album_relation (album_id, musician_id)
values (100, 41),
(101, 31),
(102, 22),
(103, 31), 
(104, 21), 
(105, 11),
(106, 32),
(107, 51),
(108, 52);

insert into genre_relation  (genre_id, musician_id) 
values (2,21),
(2, 22),
(3, 31),
(3, 32),
(5, 51),
(5, 52),
(4, 41),
(1, 11);

insert into colletion_track_relation (collection_id, track_id)
values (1, 17),
(1, 18),
(1, 19), 
(2, 20),
(2, 21),
(2, 22),
(3, 23),
(3, 24),
(3, 25),
(4, 26),
(4, 27),
(5, 28),
(5, 29),
(6, 30),
(6, 31),
(7, 19),
(7, 31),
(8, 24),
(8, 26), 
(8, 30), 
(8, 31);


update Collection
set name = 'Finally Linkin Park'
where ID = 8

insert into genre_relation (genre_id, musician_id)
values(1,31)

UPDATE colletion_track_relation 
SET track_id = 22
WHERE id = 20;

UPDATE colletion_track_relation 
SET track_id = 22
WHERE id = 14;