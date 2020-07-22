use sakila ;
#1- Afficher les 10 locations les plus longues (nom/prenom client, film, video club, durée)
SELECT CU.first_name as Prenom, CU.last_name as Nom, F.title as Film, AD.district as VideoClub, TIMESTAMPDIFF(HOUR,RE.rental_date, RE.return_date) as Duree
FROM film as F
INNER JOIN inventory as INV USING(film_id)
INNER JOIN rental as RE USING(inventory_id)
INNER JOIN customer as CU USING(customer_id)
INNER JOIN staff as ST USING(staff_id)
INNER JOIN store as STO ON STO.store_id=ST.store_id
INNER JOIN address as AD ON AD.address_id=STO.address_id
WHERE RE.return_date IS NOT NULL
ORDER BY Duree DESC LIMIT 10;

#2- Afficher les 10 meilleurs clients actifs par montant dépensé (nom/prénom client, montant dépensé)
SELECT CU.first_name as Prenom, CU.last_name as Nom, SUM(PA.amount) as Total
FROM customer as CU
INNER JOIN payment as PA ON PA.customer_id=CU.customer_id
GROUP BY CU.first_name, CU.last_name
ORDER BY Total DESC LIMIT 10;

#3- Afficher la durée moyenne de location par film triée de manière descendante
SELECT F.title as Film, AVG(TIMESTAMPDIFF(HOUR,RE.rental_date, RE.return_date)) as Duree
FROM film as F
INNER JOIN inventory as INV USING(film_id)
INNER JOIN rental as RE USING(inventory_id)
WHERE RE.return_date IS NOT NULL
GROUP BY film
ORDER BY Duree DESC;

#4- Afficher tous les films n'ayant jamais été empruntés
#Affiche les films qui n'ont jamais été emprunté dans un ou plusieurs inventaires
SELECT F.title
FROM film as F
INNER JOIN inventory as I ON F.film_id = I.film_id
LEFT JOIN rental as R on I.inventory_id = R.inventory_id
WHERE R.rental_id IS NULL;
#Affiche les films qui n'ont jamais été emprunté de manière général tout inventaire confondu, basé sur le film et non l'inventaire
#Methode 1
SELECT
(SELECT title FROM inventory INNER JOIN film ON film.film_id=inventory.film_id WHERE inventory_id=SR.inventory_id) as Titre 
FROM
 (SELECT INV.inventory_id, F.film_id from film as F
 JOIN inventory as INV ON F.film_id = INV.film_id
 LEFT JOIN rental as RE ON INV.inventory_id = RE.inventory_id
 WHERE RE.rental_id IS NULL) as SR
WHERE
 (SELECT COUNT(*) FROM rental 
 INNER JOIN inventory ON inventory.inventory_id=rental.inventory_id
 WHERE inventory.film_id=SR.film_id)=0;
#Methode 2
SELECT film.title, film.film_id FROM film 
JOIN inventory ON film.film_id = inventory.film_id
WHERE title NOT IN
(SELECT title from film 
JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IN (SELECT inventory_id FROM rental));

#5- Afficher le nombre d'employés (staff) par video club
SELECT AD.district as VideoClub, COUNT(STA.staff_id) as NbStaffPerVideoClub
FROM staff as STA
INNER JOIN store as STO USING(store_id)
INNER JOIN address as AD ON AD.address_id=STO.address_id
GROUP BY VideoClub; 
#6- Afficher les 10 villes avec le plus de video clubs
SELECT CI.city as Ville, COUNT(STO.store_id) as NbVideoClub
FROM store as STO
INNER JOIN address as AD USING(address_id)
INNER JOIN city as CI USING(city_id)
GROUP BY Ville LIMIT 10;
#7- Afficher le film le plus long dans lequel joue Johnny Lollobrigida
SELECT F.title, MAX(F.length) as Durée
FROM film as F
INNER JOIN film_actor as FA USING(film_id)
INNER JOIN actor as AC ON AC.actor_id=FA.actor_id AND AC.first_name='JOHNNY' AND AC.last_name='LOLLOBRIGIDA'
GROUP BY F.title
ORDER BY Durée DESC LIMIT 1;
#8- Afficher le temps moyen de location du film 'Academy dinosaur'
SELECT F.title as Film, AVG(TIMESTAMPDIFF(HOUR,RE.rental_date, RE.return_date)) as Duree
FROM film as F
INNER JOIN inventory as INV USING(film_id)
INNER JOIN rental as RE USING(inventory_id)
WHERE RE.return_date IS NOT NULL
AND F.title='ACADEMY DINOSAUR';
#9- Afficher les films avec plus de deux exemplaires en invenatire (store id, titre du film, nombre d'exemplaires)
SELECT INV.store_id, F.title, COUNT(INV.film_id) as NbExemplaires
FROM film as F
INNER JOIN inventory as INV USING(film_id)
GROUP BY INV.store_id, F.film_id
HAVING NbExemplaires>2;

#10- Lister les films contenant 'din' dans le titre
SELECT title
FROM film
WHERE title LIKE '%din%';

#11- Lister les 5 films les plus empruntés
SELECT F.title, COUNT(INV.film_id) as NbLocation
FROM film as F
INNER JOIN inventory as INV USING(film_id)
INNER JOIN rental as RE USING(inventory_id)
GROUP BY F.title
ORDER BY NbLocation DESC LIMIT 5;

#12- Lister les films sortis en 2003, 2005 et 2006
SELECT title, release_year
FROM film
WHERE release_year IN('2003', '2005', '2006')
ORDER BY release_year;

#13- Afficher les films ayant été empruntés mais n'ayant pas encore été restitués, triés par date d'emprunt. Afficher seulement les 10 premiers.
SELECT F.title, RE.rental_date
FROM film as F
INNER JOIN inventory as INV USING(film_id)
INNER JOIN rental as RE ON RE.inventory_id=INV.inventory_id AND RE.return_date IS NULL
ORDER BY RE.rental_date LIMIT 10;

#14- Afficher les films d'action durant plus de 2h
SELECT F.title, F.length, CA.name
FROM film as F
INNER JOIN film_category as FC USING(film_id)
INNER JOIN category as CA ON CA.category_id=FC.category_id AND CA.name='Action'
WHERE F.length>=120;
#15- Afficher tous les utilisateurs ayant emprunté des films avec la mention NC-17
SELECT CU.first_name, CU.last_name, F.title, F.rating
FROM customer as CU
INNER JOIN rental as RE USING(customer_id)
INNER JOIN inventory as INV ON INV.inventory_id=RE.inventory_id
INNER JOIN film as F ON F.film_id=INV.inventory_id AND F.rating='NC-17';
#16- Afficher les films d'animation dont la langue originale est l'anglais
SELECT F.title, CA.name, LA.name
FROM film as F
INNER JOIN film_category as FC USING(film_id)
INNER JOIN category as CA ON CA.category_id=FC.category_id AND CA.name='Animation'
INNER JOIN language as LA USING(language_id);
#17- Afficher les films dans lesquels une actrice nommée Jennifer a joué
SELECT F.title, AC.first_name, AC.last_name
FROM film as F
INNER JOIN film_actor as FA USING(film_id)
INNER JOIN actor as AC ON AC.actor_id=FA.actor_id AND AC.first_name='Jennifer';
#----(bonus: en même temps qu'un acteur nommé Johnny)
SELECT FJO.title
FROM 
	(SELECT F.film_id
	FROM film as F
	INNER JOIN film_actor as FA USING(film_id)
	INNER JOIN actor as AC ON AC.actor_id=FA.actor_id AND AC.first_name='Jennifer') as FJE
INNER JOIN 
	(SELECT F.film_id, F.title
	FROM film as F
	INNER JOIN film_actor as FA USING(film_id)
	INNER JOIN actor as AC ON AC.actor_id=FA.actor_id AND AC.first_name='Johnny') as FJO USING(film_id);

#18- Quelles sont les 3 catégories les plus empruntées?
SELECT CA.name as Categorie, COUNT(CA.category_id) as NbLocation
FROM rental as RE
INNER JOIN inventory as INV USING(inventory_id)
INNER JOIN film_category as FC USING(film_id)
INNER JOIN category as CA USING(category_id)
GROUP BY CA.name
ORDER BY NbLocation DESC LIMIT 3;

#19- Quelles sont les 10 villes où on a fait le plus de locations?
SELECT CI.city as Ville, COUNT(CI.city_id) as NbLocation
FROM rental as RE
INNER JOIN customer as CU USING(customer_id)
INNER JOIN address as AD USING(address_id)
INNER JOIN city as CI USING(city_id)
GROUP BY CI.city_id
ORDER BY NbLocation DESC LIMIT 10;

#20- Lister les acteurs ayant joué dans au moins 1 film
SELECT AC.first_name, AC.last_name, COUNT(F.film_id) as NbFilm
FROM film as F
INNER JOIN film_actor as FA USING(film_id)
INNER JOIN actor as AC USING(actor_id)
GROUP BY AC.first_name, AC.last_name
HAVING NbFilm >1
ORDER BY NbFilm;