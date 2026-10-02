SELECT income_statement.*,  car_prices.price, (income_statement.sales_revenue / car_prices.price)
S unitsSold
FROM income_statement
JOIN car_prices
ON income_statement.car_model = car_prices.car_model
