select name, year_of_issue  from album
where year_of_issue  = 2018;

select name, duration from track
where duration=(select max(duration) from track);

select name from track
where duration >= 310;

select distinct name from collection
where year_of_issue  between 2018 and 2020;

select name from musician
where name not like '% %'

select name from track
where name like '%My%' or name like '%my%' or name like '%мой%' or name like '%Мой%'