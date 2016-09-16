-- COMP9311 Assignment 2
-- Written by: Fu Zheng (Sep 2016)
-- Student Number: z3369444

-- Q1

create or replace view Q1(Name, Country) as
	SELECT name, country 
	FROM Company
	WHERE country <> 'Australia';
;
-- Q2

create or replace view Q2(Code) as
	SELECT Code
	FROM Executive
	GROUP BY Code
	HAVING COUNT(Person) >= 6;
;
-- Q3

create or replace view Q3(Name) as
	SELECT c.name
	FROM Category cat, Company c
	WHERE cat.Code = c.Code and cat.Sector = 'Technology';
;
-- Q4

create or replace view Q4(Sector, Number) as
	SELECT Sector, COUNT(Industry)
	FROM Category
	GROUP BY Sector
	ORDER BY Sector
	;
;

-- Q5!!! do I need to filter Name only??

create or replace view Q5(Name) as ...
	SELECT e.Person
	FROM Q3, Executive e, Company c 
	WHERE c.Name = Q3.Name and c.Code = e.Code
	ORDER BY e.Person;


-- Q6

create or replace view Q6(Name) as ...
	SELECT c.Name
	FROM Category cat, Company c
	WHERE cat.Code = c.Code and cat.Sector = 'Services' 
	and c.Country = 'Australia' and c.Zip LIKE '2%';


-- Q7

create or replace view Q7_1("Date", Code, Volume, Price, PrevPrice) as
	SELECT "Date", Code, Volume, Price, 
	lag(Price, 1) over (partition by Code ORDER BY "Date")
	FROM ASX;
;


create or replace view Q7("Date", Code, Volume, PrevPrice, Price, Change, Gain) as 

	SELECT "Date", Code, Volume, PrevPrice, Price,
	(Price - PrevPrice), (Price - PrevPrice)*100
	FROM Q7_1
	where "Date" <> (SELECT MIN("Date") FROM Q7_1)
	;
;
	


-- Q8

create or replace view Q8_1("Date", Volume) as
	SELECT "Date", Max(Volume)
	FROM ASX
	GROUP BY "Date";
;

create or replace view Q8("Date", Code, Volume) as

	SELECT ASX."Date", ASX.Code, ASX.Volume
	FROM ASX, Q8_1
	WHERE ASX.Volume = Q8_1.Volume AND ASX."Date" = Q8_1."Date"
	ORDER BY ASX."Date", ASX.Code
	;
;
-- Q9

create or replace view Q9_1(Industry, Number) as
	SELECT Industry, count(Code)
	FROM Category
	GROUP BY Industry;
;

create or replace view Q9(Sector, Industry, Number) as
	SELECT DISTINCT cat.Sector, cat.Industry, Q9_1.Number
	FROM Q9_1 LEFT JOIN Category cat ON (Q9_1.Industry = cat.Industry)
	ORDER BY cat.Sector, cat.Industry;
;

-- Q10

create or replace view Q10(Code, Industry) as 
	SELECT cat.Code, cat.Industry
	FROM Q9, Category cat
	WHERE Q9.Number = 1 and Q9.Industry = cat.Industry;
;
-- Q11

create or replace view Q11(Sector, AvgRating) as

	SELECT cat.Sector, AVG(r.Star) as result
	FROM Category cat, Rating r 
	WHERE cat.Code = r.Code
	GROUP BY cat.Sector
	ORDER BY result DESC;
;
-- Q12

create or replace view Q12(Name) as ...

-- Q13

create or replace view Q13(Code, Name, Address, Zip, Sector) as ...

-- Q14

create or replace view Q14(Code, BeginPrice, EndPrice, Change, Gain) as ...

-- Q15

create or replace view Q15(Code, MinPrice, AvgPrice, MaxPrice, MinDayGain, AvgDayGain, MaxDayGain) as ...

-- Q16


-- Q17


-- Q18



