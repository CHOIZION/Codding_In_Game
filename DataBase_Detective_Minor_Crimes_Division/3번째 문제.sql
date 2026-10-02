SELECT *
FROM bureaucon
JOIN dumbcon
On bureaucon.attendee_id = dumbcon.attendee_id

SELECT *
FROM Suspects
WHERE forms_brought = 8
AND dumbs_brought = 10

SELECT *
FROM attendees 
WHERE id = "이전에 쓴 SQL 문으로 나온 ID 넣기"