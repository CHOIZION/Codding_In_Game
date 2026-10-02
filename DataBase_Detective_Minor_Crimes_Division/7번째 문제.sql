SELECT *
FROM phil_hwk
JOIN phil_ZoranAll
ON Phil_hwk.philosopher = phil_ZoranAll.directly_influenced

SELECt subject_name, SUM(queries_written) AS totQueries
FROM sci_hwk
WHERE age < 21
GROUP BY subject_Name

SELECT s2.*, s2.queries_written -
s1.queries_written AS delta
FROM sci_hwk s1
JOIN sci_hwk s2
ON s1.age + 1 = s2.age
AND s1.subject_name = s2.subject_name

SELECT SeatsnScores.*, daysAtClass.daysAttended
FROM SeatsNScores
JOIN daysAtClass
ON SeatsNScores.student_id = daysAtClass.student_id

SELECT *
FROM topPerformers
JOIN badAttendance
ON topPerformers.seat_number + 1 = badAttendedance.seat_number
AND topPerformers.row = badAttendance.row
ANd topPerformers.score > 76 + badAttendance.score