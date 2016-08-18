-- COMP9311 16s2 Assignment 1
-- Schema for KensingtonCars
--
-- Written by <<YOUR NAME GOES HERE>>
-- Student ID: <<YOUR STUDENT NUMBER>>
--

-- Some useful domains; you can define more if needed.

create domain URLType as
	varchar(100) check (value like 'http://%');

create domain EmailType as
	varchar(100) check (value like '%@%.%');

create domain PhoneType as
	char(10) check (value ~ '[0-9]{10}');


-- EMPLOYEE

create table Employee (
	EID          serial, 
    FirstName	 text,
    LastName 	 text,
    Salary       integer not null check (Salary > 0),
    TFN			 integer,
	primary key (EID)
);

create table Admin (
	EID			serial references Employee(EID),
	primary key (EID)

);

create table Mechanic (
	EID			serial references Employee(EID),
	License 	text,
	primary key (EID)
);

create table Salesman (
	EID			serial references Employee(EID),
	CommRate 	text,
	primary key (EID) 	
);

-- CLIENT

create table Client (
	CID          serial,
	Name 		 text,
	Address  	 text,
	Phone 		 PhoneType,
	Email 		 EmailType,
	primary key (CID)
);

create table Company (
	CID 		 serial references Client(CID),
	URL 		 URLType,
	ABN  		 text,
	primary key (CID)
);


-- CAR

create domain CarLicenseType as
        char(6) check (value ~ '[0-9A-Za-z]{6}');

create domain OptionType as varchar(12)
	check (value in ('sunroof','moonroof','GPS','alloy wheels','leather'));

create domain VINType as char(17) check ...