SELECT *
FROM timesheet
JOin cops
on timesheet.badge_number = cops.badge_number
where cops.security_level = 3
And timesheet.checkout_time > 2200
And guns_issued = 1