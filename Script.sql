create table if not exists Genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);
create table if not exists Musician (
	id INTEGER PRIMARY KEY,
	name VARCHAR(40) not NULL 
);
create table if not exists Genre_Relation (
	id SERIAL PRIMARY KEY,
	Genre_id INTEGER NOT NULL REFERENCES Genre(id),
	Musician_id INTEGER NOT NULL REFERENCES Musician(id)
 );
create table if not exists Album (
	id INTEGER PRIMARY KEY,
	name VARCHAR(40) not null,
	year_of_issue INTEGER NOT NULL
);
create table if not exists Album_Relation (
	id SERIAL PRIMARY KEY,
	Album_id INTEGER NOT NULL REFERENCES Album(id),
	Musician_id INTEGER NOT NULL REFERENCES Musician(id)
 );
create table if not exists Collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT null,
	year_of_issue INTEGER NOT null
);
create table if not exists Track (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT null,
	duration INTEGER NOT null,
	Album_id INTEGER NOT NULL REFERENCES Album(id),
	Collection_id INTEGER NOT NULL REFERENCES Collection(id)
);
