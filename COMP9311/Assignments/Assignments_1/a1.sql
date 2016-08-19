-- COMP9311 16s2 Assignment 1
-- Schema for KensingtonCars
--
-- Written by FU ZHENG
-- Student ID: z3369444
--

-- Some useful domains; you can define more if needed.

create domain URLType as
	varchar(100) check (value like 'http://%');

create domain EmailType as
	varchar(100) check (value like '%@%.%');

create domain PhoneType as
	char(10) check (value ~ '[0-9]{10}');

create domain CarLicenseType as
    char(6) check (value ~ '[0-9A-Za-z]{6}');

create domain OptionType as 
	varchar(12)	check (value in ('sunroof','moonroof','GPS','alloy wheels','leather'));

create domain VINType as 
	char(17) check (value ~ '[A-Z0-9]{17}' and value !~ '[IOQ]');  -- need to be fixed with upper case only

create domain MonetaryType as 
	numeric(8,2) check (value >= 0);  --2 decimal digits, not exceed 6 integral digits ??


-- EMPLOYEE

create table Employee (
	EID          serial, 
    firstname	 varchar(50) not null,
    lastname 	 varchar(50) not null,
    salary       integer not null check (salary > 0),
    TFN			 char(9) not null constraint ValidTFN check (TFN ~ '[0-9]{9}'),
	primary key (EID)
);

create table Admin (
	EID			serial references Employee(EID),
	primary key (EID)

);

create table Mechanic (
	EID			serial references Employee(EID),
	license 	char(8) not null check (license ~ '[0-9A-Za-z]{8}'),
	primary key (EID)
);

create table Salesman (
	EID			serial references Employee(EID),
	commRate 	integer not null constraint ValidCommRate check (commRate >= 5 and commRate <= 20),
	primary key (EID) 	
);

-- CLIENT

create table Client (
	CID          serial,
	name 		 varchar(100) not null,
	address  	 varchar(200) not null,
	phone 		 PhoneType not null,
	email 		 EmailType,
	primary key (CID)
);

-- COMPANY

create table Company (
	CID 		 serial references Client(CID),
	url 		 URLType,
	ABN  		 char(11) not null constraint ValidABN check (ABN ~ '[0-9]{11}'), --need to check the boolean condition
	primary key (CID)
);


-- CAR


create table Car (
	VIN 		 VINType,		
	manufacturer varchar(40) not null,
	model 		 varchar(40) not null,
	year		 integer not null constraint ValidYear check (year >= 1970 and year <= 2099),		--double check with type
	primary key (VIN)
);

-- OPTIONS

create table Options (
	VIN 		 VINType,
	options      OptionType,
	primary key (VIN, options),
	foreign key (VIN) references Car(VIN)
);

-- NEWCAR

create table NewCar (
	VIN 		  VINType references Car(VIN),
	cost 		  MonetaryType not null,			-- should this be numeric or money???
	charges  	  MonetaryType not null,
	seller	   	  serial,							-- partial participation
	"date"	 	  date not null,
	price 	  	  MonetaryType not null,
	commission 	  MonetaryType not null,
	plateNumber   varchar(6) not null,
	primary key (VIN),
	foreign key (seller) references Salesman(EID)
);

-- USEDCAR

create table UsedCar (
	VIN  		 VINType references Car(VIN),
	plateNumber  varchar(6) not null,
	seller		 serial,							-- partial participation
	buyer 	 	 serial,							-- partial participation
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	primary key (VIN),
	foreign key (seller) references Salesman(EID),
	foreign key (buyer) references Salesman(EID)
);

-- Repair Job

create table RepairJob (
	VIN			 VINType,
	"number"  	 integer  check ("number" >= 1 and "number" <= 999),
	description  varchar(250) not null,
	parts  		 MonetaryType not null,
	work 		 MonetaryType not null,
	"date"  	 date not null,
	repairs 	 VINType not null,
	paidBy 		 serial not null,
	primary key (VIN, "number"),
	foreign key (VIN) references Car(VIN),
	foreign key (repairs) references UsedCar(VIN),
	foreign key (paidBy) references Client(CID)
);

create table Does (
	EID			 serial,
	VIN			 VINType,
	"number"  	 integer  check ("number" >= 1 and "number" <= 999),
	primary key (EID, VIN, "number"),
	foreign key (EID) references Mechanic(EID),
	foreign key (VIN, "number") references RepairJob(VIN, "number")

);

create table Buys (
	owner 	  	 serial,		--seller
	VIN  		 VINType,
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	primary key (owner, VIN),
	foreign key (owner) references Client(CID),
	foreign key (VIN) references Car(VIN)
	

);

create table Sells (

	owner 	  	 serial,		-- buyer
	VIN  		 VINType,
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	primary key (owner, VIN),
	foreign key (owner) references Client(CID),
	foreign key (VIN) references Car(VIN)

);

create table SellsNew (

	owner 	  	 serial,		-- buyer
	VIN  		 VINType,
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	plateNumber  varchar(6) not null,
	primary key (owner, VIN),
	foreign key (owner) references Client(CID),
	foreign key (VIN) references Car(VIN)

);