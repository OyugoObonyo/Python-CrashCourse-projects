-- Get David's start times

SELECT starttime FROM cd.bookings
JOIN cd.members
ON cd.bookings.memid = cd.members.memid 
WHERE cd.members.firstname = 'David' 
AND cd.members.surname = 'Farrell'