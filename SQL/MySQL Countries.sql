/*1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. 
Your query should arrange the result by language percentage in descending order. (1)
*/
use world;
select cn.name as country, ln.language, ln.percentage
from countries cn left join
languages ln on cn.id = ln.country_id where ln.language = "Slovene" 
order by ln.percentage DESC;


/*
2. What query would you run to display the total number of cities for each country? 
Your query should return the name of the country and the total number of cities. 
Your query should arrange the result by the number of cities in descending order. (3)
*/

select countries.name as countries, count(cities.name) as cities
from countries left join cities
on countries.id = cities.country_id
group by countries.name
order by cities desc;


/*
3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? 
Your query should arrange the result by population in descending order. (1)
*/

select c.name, c.population from cities c
join countries ct on ct.id = c.country_id
where ct.name = "Mexico" and c.population >500000;




/*
4. What query would you run to get all languages in each country with a percentage greater than 89%? 
Your query should arrange the result by percentage in descending order. (1)
*/

select c.name, ln.language, ln.percentage
from countries c left join
languages ln on c.id = ln.country_id 
where ln.percentage >89
order by ln.percentage DESC;

/*
5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
*/
select name, surface_area, population from countries
where surface_area < 501 and population > 100000 ;

/*
6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 
and a life expectancy greater than 75 years? (1)
*/
select name, government_form, capital, life_expectancy from countries
where government_form = "Constitutional Monarchy" and capital > 200 and life_expectancy>75;


 /*
7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
*/
select "Argentina" as name, name, district, population from cities
where population > 500000  and district = "Buenos Aires";
/*
8. What query would you run to summarize the number of countries in each region? 
The query should display the name of the region and the number of countries. 
Also, the query should arrange the result by the number of countries in descending order. (2)*/

select region, count(*) as countries from countries
group by region
order by countries desc;