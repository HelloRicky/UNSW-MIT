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
	HAVING COUNT(Person) > 5;
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
	GROUP BY Sector;
;

-- Q5!!!

create or replace view Q5(Name) as ...
	SELECT e.Person
	FROM Q3, Executive e, Company c 
	WHERE c.Name = Q3.Name and c.Code = e.Code;


-- Q6

create or replace view Q6(Name) as ...
	SELECT c.Name
	FROM Category cat, Company c
	WHERE cat.Code = c.Code and cat.Sector = 'Services' 
	and c.Country = 'Australia' and c.Zip LIKE '2%';

-- Q7!!!

create or replace view Q7("Date", Code, Volume, PrevPrice, Price, Change, Gain) as ...

	SELECT MAX("Date"), Code
	FROM ASX
	GROUP BY Code;

-- Q8!!!

create or replace view Q8("Date", Code, Volume) as ...

	SELECT "Date"
	FROM ASX
	GROUP BY "Date"
	ORDER BY "Date" and Code;

-- Q9

create or replace view Q9(Sector, Industry, Number) as ...

-- Q10

create or replace view Q10(Code, Industry) as ...

-- Q11

create or replace view Q11(Sector, AvgRating) as ...

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



