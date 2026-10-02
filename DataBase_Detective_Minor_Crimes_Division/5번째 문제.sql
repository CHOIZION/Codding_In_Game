SELECT *
FROM web_searches
WHERE ip_address = "주소"
ORDER BY time_visited ASC

SELECT *
FROM ribbit78_10s
JOIN movies
ON ribbit78_10s.title = movies.title

SELECT director
FROM movies
GROUP BY director
HAVING MAX(rating) < 8.5

SELECT order_74b8s.*, nutrition_facts.nutrient, nutrition_facts.nutrient_quantity,(nutrient_quantity * quantity_purchased) AS totalNutirent
FROM order_74b8s
JOIN nutrition_facts
ON order_74b8s.item_name = nutrition_facts.item_name
ORDER BY nutrient