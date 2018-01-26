/*
1. What query would you run to get the total revenue for March of 2012?
*/ 
select "March" as month, sum(amount) from billing where charged_datetime like "%2012-03-%";

/*
2. What query would you run to get total revenue collected from the client with an id of 2?
*/ 

select clients.client_id, sum(amount) from billing
join clients on billing.client_id = clients.client_id
where clients.client_id = 2;

/*
3. What query would you run to get all the sites that client=10 owns?
*/

select domain_name as websites, client_id from sites where client_id = 10;

 /*
4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
*/ 
select count(domain_name), MONTHNAME(created_datetime), year(created_datetime) from sites
where MONTH(created_datetime) and client_id=1
group by created_datetime;

/*
5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
*/ 

select s.domain_name,  registered_datetime from leads l
join sites s on s.site_id = l.site_id
where registered_datetime between '2011-01-01' and '2011-02-15'
order by registered_datetime;

/*
6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
*/

select concat(c.first_name, ' ', c.last_name) as client_name, count(l.leads_id) as number_of_lead
from clients c
left join sites s on c.client_id = s.client_id
left join leads l on l.site_id = s.site_id
where registered_datetime between '2011-01-01' and '2011-12-31'
group by client_name;

 /*
7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
*/ 

select concat(c.first_name, ' ',c.last_name) as client_name, count(l.leads_id) as number_of_lead, MONTHNAME(l.registered_datetime) as months
from clients c
join sites s on c.client_id = s.client_id
join leads l on l.site_id = s.site_id
where l.registered_datetime between '2011-01-01' and '2011-07-1'
group by c.client_id, MONTHNAME(l.registered_datetime)
ORDER BY MONTH(l.registered_datetime);

/*
8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites 
between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all 
the clients, the site name(s), and the total number of leads generated from each site for all time.
*/ 

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_generated
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.domain_name;

/*
9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
*/ 
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS monthly_revenue, DATE_FORMAT(billing.charged_datetime, '%M') AS 'month', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'year'
FROM clients
	LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)
ORDER BY clients.client_id;

/*
10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
*/

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS 'sites'
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;