use sakila;

/*
1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.
*/

select c.first_name, c.last_name, c.email, a.address from customer c
join address a on c.address_id = a.address_id
where a.city_id = 312;

/*
2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).
*/ 
select f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, "Comedy" as genre from film f
join film_category c on f.film_id = c.category_id
join category ct on ct.category_id = c.category_id
where ct.name = "Comedy";

/*
3. What query would you run to get all the films joined by actor_id=5? 
Your query should return the actor id, actor name, film title, description, and release year.
*/ 

select film_actor.actor_id, CONCAT(actor.first_name , ' ', actor.last_name) as actor_name, film.film_id, title, description, release_year from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where actor.actor_id = 5;

/*
4. What query would you run to get all the customers in store_id = 1 and 
inside these cities (1, 42, 312 and 459)? Your query should return customer 
first name, last name, email, and address.
*/ 

select customer.store_id, city.city_id, customer.first_name, customer.last_name, email, address.address from customer
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where customer.store_id = 1 and city.city_id in (1,42,312,459)
order by city_id;


/*
5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.
*/
select title, description, release_year, rating, special_features from film
where rating = "G" and special_features LIKE '%behind the scenes%'
and film_id in(select film_id from film_actor where actor_id = 15);

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
	JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = 'G'
	AND film.special_features LIKE '%behind the scenes%'
	AND actor.actor_id = 15;

/*
6. What query would you run to get all the actors that joined in the film_id = 369?
Your query should return the film_id, title, actor_id, and actor_name.
*/

select fl.film_id as filmID, fl.title, film_actor.actor_id, concat(actor.first_name,' ', actor.last_name) as actor_name from actor
join film_actor on actor.actor_id = film_actor.actor_id
join film fl on fl.film_id = film_actor.film_id
where fl.film_id = 369;

/*
7. What query would you run to get all drama films with a rental rate of 2.99? 
Your query should return film title, description, release year, rating, special features, 
and genre (category).
*/
select f.film_id, f.title, f.description, f.release_year, f.rating, f.special_features, c.name, f.rental_rate from film f
join film_category on f.film_id = film_category.film_id
join category c on c.category_id = film_category.category_id
where rental_rate = 2.99 and c.name= 'Drama';

/*
8. What query would you run to get all the action films which are joined by SANDRA KILMER? 
Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
*/
select f.title, f.description,f.release_year, f.rating,
f.special_features, c.name, "SANDRA KILMER" as actor
from film f
join film_category on f.film_id = film_category.film_id
join category c on c.category_id = film_category.category_id
join film_actor on film_actor.film_id = f.film_id
where c.name= 'action' and film_actor.actor_id in 
(Select actor_id from actor where first_name = "sandra" and last_name = "kilmer");

