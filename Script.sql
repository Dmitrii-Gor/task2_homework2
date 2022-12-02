create table if not exists Genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) not null
);
create table if not exists Musician (
	id INTEGER PRIMARY KEY,
	name VARCHAR(40) not null
);
create table if not exists Genre_Relation (
	id SERIAL PRIMARY KEY,
	Genre_id INTEGER not null REFERENCES Genre(id),
	Musician_id INTEGER not null REFERENCES Musician(id)
 );
create table if not exists Album (
	id INTEGER PRIMARY KEY,
	name VARCHAR(40) not null,
	year_of_issue INTEGER not null,
	check (year_of_issue > 1900)
);
create table if not exists Album_Relation (
	id SERIAL PRIMARY KEY,
	Album_id INTEGER not null REFERENCES Album(id),
	Musician_id INTEGER not null REFERENCES Musician(id)
 );
create table if not exists Collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) not null,
	year_of_issue INTEGER not null,
	check (year_of_issue > 1900)
);
create table if not exists Track (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) not null,
	duration INTEGER not null,
	check (duration < 600),
	Album_id INTEGER NOT NULL REFERENCES Album(id)
);
create table if not exists Colletion_Track_Relation (
	id SERIAL PRIMARY KEY,
	Collection_id INTEGER not null references Collection(id),
	Track_id INTEGER not null REFERENCES Track(id)
 );