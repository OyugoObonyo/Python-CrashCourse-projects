-- Get tennis courts available on 21/9/2012

SELECT starttime, cd.facilities.name FROM cd.bookings
JOIN cd.facilities
ON cd.bookings.facid = cd.facilities.facid 
WHERE cd.facilities.name IN ('Tennis Court 1', 'Tennis Court 2')
AND starttime >= '2012-09-21' 
AND starttime <= '2012-09-22'