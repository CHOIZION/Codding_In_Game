SELECT mail_trans.*, mail_prices.price
FROM mail_trans
JOIN mail_prices
On mail_trans.date = mail_prices.date
WHERE mail_prices.date <= 아이디

SELECT *
FROM flights
WHERE time > 아이디
AND time < 아이디
AND arriving = "Flushing"

SELECT *
FROM flushFlights
JOIN games_history
ON flushFlights.date = games_history.date
WHERE games_history.team = "Uncles"

SELECT packages_melissasalerno.address
FROM packages_melissasalerno
JOIN packages_trenttubey
ON packages_melissasalerno.address = packages_trenttubey.address
WHERE packages_melissasalerno.delivery_type = "OUTGOING"

SELECT alin_buyers.totalBuy - alin_sellers.totalSell AS netShares, alin_buyers.buyer
FROM alin_buyers
JOIN alin_sellers
ON alin_buyers.buyer = alin_sellers.seller
ORDER BY netShares DESC