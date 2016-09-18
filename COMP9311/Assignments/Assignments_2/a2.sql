-- COMP9311 Assignment 2
-- Written by: Fu Zheng (Sep 2016)
-- Student Number: z3369444


-- Q1: List all the company names (and countries) that are incorporated outside Australia.

create or replace view Q1(Name, Country) as
	select name, country 
	from Company
	where country <> 'Australia'				-- any contry is not Australia will be exluced.
;

-- Q2: List all the company codes that have more than five executive members on record (i.e., at least six).

create or replace view Q2(Code) as
	select Code
	from Executive
	group by Code 								-- group data by company code
	having COUNT(Person) >= 6 					-- any company has at least 6 people
;

-- Q3: List all the company names that are in the sector of "Technology"

create or replace view Q3(Name) as
	select c.name
	from Category cat, Company c
	where cat.Code = c.Code 					-- Tables joint by code
	and cat.Sector = 'Technology' 				-- only in 'technology' sector
;

-- Q4: Find the number of Industries in each Sector

create or replace view Q4(Sector, Number) as
	select Sector, COUNT(Distinct Industry)     -- some industries can be same, hence use Distinct to remove duplicated item
	from Category
	group by Sector 							-- group data by sector
	order by Sector 							-- order result by sector in ascending(default)
;

-- Q5: Find all the executives (i.e., their names) that are affiliated with companies in the sector of "Technology". 

create or replace view Q5(Name) as
	select Distinct e.Person 					-- some person may affiliated multiple company, hence use Distinct to remove duplicated name
	from Q3, Executive e, Company c  			-- Q3 contains all the company in the sector of 'technology'
	where c.Name = Q3.Name 						-- Tables joint by Name
	and c.Code = e.Code 						-- and Tables joint by Code
	order by e.Person 							-- order result by person's name in ascending(default)
;

-- Q6: List all the company names in the sector of "Services" that are located in Australia with the first digit of their zip code being 2.

create or replace view Q6(Name) as 
	select c.Name
	from Category cat, Company c
	where cat.Code = c.Code  					-- Tables joint by Code
	and cat.Sector = 'Services' 				-- only interested in the 'Services' sector
	and c.Country = 'Australia' 				-- and for all the Australian company
	and c.Zip LIKE '2%'							-- postcode started with number '2'
;


-- Q7: Create a database view of the ASX table that contains previous Price, Price change (in amount, can be negative) and Price gain (in percentage, can be negative). 

create or replace view Q7_1("Date", Code, Volume, Price, PrevPrice) as
	select "Date", Code, Volume, Price, 		-- create temp view to store daily previous price for each company
	lag(Price, 1, null) 						-- use lag function to offset Price value by 1 and
	over (partition by Code order by "Date") 	-- store into PrevPrice value for each company order by "Date"
	from ASX
;


create or replace view Q7("Date", Code, Volume, PrevPrice, Price, Change, Gain) as 
	select "Date", Code, Volume, PrevPrice, Price,
	(Price - PrevPrice), 						-- calculate Price change (in amount, can be negative) 
	(Price - PrevPrice)/PrevPrice * 100			-- calculate Price gain (in percentage, can be negative)
	from Q7_1
	where PrevPrice is not null 				-- exclude tuples on the frist day where null value generated after offset in Lag function
;

-- Q8: Find the most active trading stock (the one with the maximum trading volume; if more than one, output all of them) on every trading day. Order your output by "Date" and then by Code.

create or replace view Q8_1("Date", Volume) as 	-- create temp view to group data by date
	select "Date", MAX(Volume)				   	-- find out the max volume of each date across all company
	from ASX
	group by "Date"								-- group data by "Date"
;

create or replace view Q8("Date", Code, Volume) as
	select ASX."Date", ASX.Code, ASX.Volume
	from ASX, Q8_1
	where ASX.Volume = Q8_1.Volume 				-- Tables joint by volume
	and ASX."Date" = Q8_1."Date" 				-- also joint by "Date"
	order by ASX."Date", ASX.Code 				-- order output by "Date" and then by Code in ascending(default).
;

-- Q9: Find the number of companies per Industry. Order your result by Sector and then by Industry.

create or replace view Q9(Sector, Industry, Number) as
	select Sector, Industry, COUNT(*) 			-- aggregate the total number of company with COUNT function after grouping
	from category
	group by Sector, Industry 					-- group data by Sector and then by Industry
	order by Sector, Industry 					-- order output by Sector and then by Industry in ascending(default).
;

-- Q10: List all the companies (by their Code) that are the only one in their Industry (i.e., no competitors).

create or replace view Q10(Code, Industry) as 
	select cat.Code, cat.Industry
	from Q9, Category cat
	where Q9.Number = 1 						-- if there is one company in the industry
	and Q9.Industry = cat.industry 				-- Tables joint by industry
;

-- Q11: List all sectors ranked by their average ratings in descending order. 

create or replace view Q11(Sector, AvgRating) as
	select cat.Sector, AVG(r.Star) as result   	-- average rating with AVG function
	from Category cat, Rating r 
	where cat.Code = r.Code 					-- Tables joint by Code
	group by cat.Sector 						-- group data by Sector
	order by result DESC  						-- order output by average rating in descending order
;

-- Q12: Output the person names of the executives that are affiliated with more than one company.

create or replace view Q12(Name) as
	select Person
	from Executive
	group by Person 							-- group data by Person
	having COUNT(Code) > 1 						-- count the total company affiliated per person and if it is more than one
;


-- Q13: Find all the companies with a registered address in Australia, in a Sector where there are no overseas companies in the same Sector. 

create or replace view Q13_1(Sector) as  		-- create temp View to find out all the sectors that contain the company are incorporated outside Australia
	select DISTINCT cat.Sector 					-- remove duplicated sector
	from Company c, Q1, Category cat 			-- Q1 contains all companies incorporated outside Australia
	where c.Name = Q1.Name  					-- Tables joint by Name 
	and c.Code = cat.Code 	 					-- and Tables joint by Code
;

create or replace view Q13(Code, Name, Address, Zip, Sector) as 
	select c.Code, c.Name, c.Address, c.Zip, cat.Sector
	from Company c, Category cat
	where c.Code = cat.Code  					-- Tables joint by Code
	and c.Country = 'Australia' 				-- and only for company incorporated inside Australia
	and Not exists (select * from Q13_1  		-- and no oversea company (Q13_1 contain all oversea companies) exist in sector
	where Q13_1.Sector = cat.Sector) 			-- matching sector in the sub-query
;
-- Q14: Calculate stock gains based on their prices of the first trading day and last trading day (i.e., the oldest "Date" and the most recent "Date" of the records stored in the ASX table). 

create or replace view Q14_1(Code, StartDate, EndDate) as
	select Code, MIN("Date"), MAX("Date") 		-- create temp View to hold startDate (MIN) and endDate (MAX) for each company
	from ASX
	group by Code 								-- group data by each company code
;

-- StartDate Price
create or replace view Q14_2(Code, StartDate, Price) as
	select ASX.Code, Q14_1.StartDate, ASX.Price -- create View to hold startDate price
	from ASX, Q14_1
	where ASX.Code = Q14_1.Code  				-- Tables joint by Code
	and ASX."Date" = Q14_1.StartDate 			-- and "Date" is the startDate of each Code
;

-- EndDate price
create or replace view Q14_3(Code, EndDate, Price) as
	select ASX.Code, Q14_1.EndDate, ASX.Price 	-- create View to hold startDate price
	from ASX, Q14_1
	where ASX.Code = Q14_1.Code 				-- Tables joint by Code
	and ASX."Date" = Q14_1.EndDate 				-- and "Date" is the EndDate of each Code
;

create or replace view Q14(Code, BeginPrice, EndPrice, Change, Gain) as 
	select Q14_2.Code , Q14_2.Price, Q14_3.Price,
	(Q14_3.Price - Q14_2.Price), 				-- Calculate Price change from endDate to startDate
	(Q14_3.Price - Q14_2.Price)/Q14_2.Price * 100 as GainVal
	from Q14_2, Q14_3
	where Q14_2.Code = Q14_3.Code 				-- Tables joint by Code
	order by GainVal DESC, Q14_2.Code			-- order output by value gain in descending order and then company code in ascending(default)
;


-- Q15: For all the trading records in the ASX table, produce the following statistics as a database view (where Gain is measured in percentage). 

create or replace view Q15_1(Code, MinPrice, MaxPrice, SumPrice, MinDayGain, MaxDayGain, SumDayGain, SumGainDays) as
	select Code, 								-- create temp View to hold Min& Max value of price and gain, total of days of each stock in the market
	case										-- define Min price in all time
		when MIN(Price) < Min(PrevPrice) then MIN(Price) --Price column include the end date price
		else MIN(PrevPrice) 					-- since PrevPrice recorded 1st day price, use condition check to include 1st day price
	end,
	case 										-- define Max price in all time
		when MAX(Price) > MAX(PrevPrice) then MAX(Price)
		else MAX(PrevPrice) 					-- similar to Min price case
	end,
	SUM(Price), 								-- Summation of all the daily price, exlude the first day price
	MIN(Gain), 									-- Min daily gain in all time of each stock
	MAX(Gain),  								-- Max daily gain in all time of each stock
	SUM(Gain), 									-- Summation of gains in all time of each stock
	COUNT("Date") 								-- number of days of each stock on the market, exclude the first day
	from Q7
	group by Code 								-- group data by company Code
;

create or replace view Q15(Code, MinPrice, AvgPrice, MaxPrice, MinDayGain, AvgDayGain, MaxDayGain) as 
	select Q15_1.Code, 							-- Code
	Q15_1.MinPrice, 							-- MinPrice
	(Q15_1.SumPrice + Q14.BeginPrice)/(Q15_1.SumGainDays + 1), -- AvgPrice: add price of the start day
	Q15_1.MaxPrice, 							-- MaxPrice
	Q15_1.MinDayGain, 							-- MinDayGain
	Q15_1.SumDayGain/Q15_1.SumGainDays, 		-- AvgDayGain,
	Q15_1.MaxDayGain 							-- MaxDayGain
	from Q15_1, Q14
	where Q15_1.Code = Q14.Code 				-- Tables joint by Code
;

-- Q16: Create a trigger on the Executive table, to check and disallow any insert or update of a Person in the Executive table to be an executive of more than one company. 

create or replace function 						-- create function checkExecutive() for trigger
	checkExecutive() returns trigger 
as $$
declare
	e Executive; 								-- define variable e to store query
begin 
	select * into e from Executive 
	where Person = new.Person; 					-- find out all record with give person name

	-- make use of the special variable TG_OP to work out the operation.
	-- for insert
	if (TG_OP = 'INSERT') then
		if (COUNT(e.Code) = 0) then 			-- if no record exits
			return new; 						-- allow and return New
		end if; 								-- if record exit then raise error message
 		raise exception 'Person exists in %', e.Code;

	-- for update
	elsif (TG_OP = 'UPDATE') then
		if (COUNT(e.Code) < 2) then 			-- if output = 1, user attempts to update Code only, if output = 0, user attempt to update New person
			return new;
		end if;
		raise exception 'Person exists in %', e.Code;
	end if;
	return null; 								-- result is ignored since this is an AFTER trigger
end;
$$ language plpgsql;

create trigger checkExecutive
before insert or update on Executive  			-- trigger before INSERT or Update take place
for each row execute procedure checkExecutive();

-- Q17: Create a trigger to increase the stock's rating (as Star's) to 5 when the stock has made a maximum daily price gain (when compared with the price on the previous trading day) in percentage within its sector.

create or replace View Q17_1("Date", Code, Sector, Gain) as --create temp View to store Sector for each stock
	select Q7."Date", Q7.Code, cat.Sector, Q7.Gain 
	from Q7, Category cat
	where Q7.Code = cat.Code
;

create or replace function 						-- create function updateStart() for trigger
	updateStart() returns trigger
as $$
declare											-- define all the variables for Max, Min and New gain
	Gain_Max numeric default 0;
	Gain_Min numeric default 0;
	Gain_New numeric default 0;
begin
	select Max(Gain), Min(Gain) into Gain_Max, Gain_Min from Q17_1 -- store query result into max and min gain variables
	where "Date" = new."Date" 
	and Q17_1.Sector = (select Distinct Sector from Q17_1 where Code = new.Code); --identify sector of stock

	select Gain into Gain_New from Q17_1 		-- store query result into Gain_New variable for daily price
	where "Date" = new."Date" 
	and Code = new.Code; 

	if(Gain_New >= Gain_Max) then 				-- if daily price is greater or equal to max previous price in the sector
		update Rating 							-- update start to 5 of input code
		set Star = 5
		where Rating.Code = new.Code;
	end if;

	if(Gain_New <= Gain_Min) then 				-- if daily price is less or equal to min previous price in the sector
		update Rating 							-- update start to 1 of input code
		set Star = 1
		where Rating.Code = new.Code;
	end if;
	
	return new; 								-- continue
end
$$ language plpgsql;

create trigger updateStart 
after insert on ASX 							-- trigger after more data been inserted
for each row execute procedure updateStart();

-- Q18: Create a trigger to log any updates on Price and/or Voume in the ASX table and log these updates (only for update, not inserts) into the ASXLog table.

create or replace function 						-- create function updateASX() for trigger
	updateASX() returns trigger
as $$
begin
	insert into ASXLog 							-- insert record into ASXLog table
	values(Now(), new."Date", new.Code, old.Volume, old.Price);
	return new;
end
$$ language plpgsql;

create trigger updateASX
after update on ASX 							-- trigger after ASX record been updated
for each row execute procedure updateASX();