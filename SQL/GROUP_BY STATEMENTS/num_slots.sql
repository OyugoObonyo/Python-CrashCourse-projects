-- Total number of slots booked per facility in sepetember 2012

SELECT facid, SUM(slots) FROM cd.bookings
WHERE EXTRACT(MONTH FROM starttime) = 9 
AND EXTRACT(YEAR FROM starttime) = 2012
GROUP by facid
ORDER BY SUM(slots)