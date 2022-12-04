select genre.name, count(musician.name) from musician
join genre_relation on musician.id = genre_relation.musician_id
join genre on genre.id = genre_relation.genre_id
group by genre.name
order by count(musician.name)

select album.name, count(track.name) from track
join album on album.id = track.album_id
where album.year_of_issue >= 2019 and album.year_of_issue <= 2020
group by album.name
order by count(track.name)

select album.name, avg(track.duration) from track
join album on album.id = track.album_id
group by album.name
order by avg(track.duration) desc

select musician.name from musician
where musician.name not in (select musician.name from musician 
join album_relation on musician.id = album_relation.musician_id
join album on album_relation.album_id = album.id
where (album.year_of_issue = 2020))

select collection.name from collection
where name like '%Linkin Park%'

select album.name from musician 
join genre_relation on musician.id = genre_relation.musician_id
join genre on genre.id = genre_relation.genre_id
join album_relation on musician.id = album_relation.musician_id
join album on album.id = album_relation.album_id
group by album.name, musician.name
having count(genre.name) > 1
order by count(genre.name)

select track.name from collection
full join colletion_track_relation on collection.id = colletion_track_relation.collection_id
full join track on track.id = colletion_track_relation.track_id
where collection.name is null

select musician.name, track.duration from track
join album on track.album_id = album.id
join album_relation on album.id = album_relation.album_id 
join musician on musician.id = album_relation.musician_id
where track.duration = (select min(track.duration) from track)
order by track.duration

select album.name from album
join track on track.album_id = album.id 
group by album.name
having count(track.name) = (select count(track.name) from track 
join album on album.id = track.album_id
group by album.name
order by count(track.name) limit 1)
order by count(track.name)