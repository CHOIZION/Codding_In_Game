SELECT Order Totals.*, tips. dollars_tipped, tips.dollars_tipped / OrderTotals.total AS ratio
FROM Sus_Orders
JOIN OrderTotals, tips
ON Sus_Orders.order_number = ORder Totals.order_number AND
Sus_Orders.order_number = tips.order_number
ORDER BY ratio ASC