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
	char(17) check (value ~ '[A-Z0-9]{17}' and value !~ '[IOQ]'); 

create domain MonetaryType as 
	numeric(8,2) check (value >= 0); 


-- EMPLOYEE

create table Employee (
	EID          serial, 
    firstname	 varchar(50) not null,
    lastname 	 varchar(50) not null,
    salary       integer not null constraint ValidSalary check (salary > 0),
    TFN			 char(9) not null constraint ValidTFN check (TFN ~ '[0-9]{9}'),
	primary key (EID)
);

create table Admin (
	EID			 serial references Employee(EID),
	primary key (EID)

);

create table Mechanic (
	EID			 serial references Employee(EID),
	license 	 char(8) not null constraint ValidLicense check (license ~ '[0-9A-Za-z]{8}'),
	primary key (EID)
);

create table Salesman (
	EID			 serial references Employee(EID),
	commRate 	 integer not null constraint ValidCommRate check (commRate >= 5 and commRate <= 20),
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
	ABN  		 char(11) not null constraint ValidABN check (ABN ~ '[0-9]{11}'),
	primary key (CID)
);


-- CAR


create table Car (
	VIN 		 VINType,		
	manufacturer varchar(40) not null,
	model 		 varchar(40) not null,
	year		 integer not null constraint ValidYear check (year >= 1970 and year <= 2099),
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
	cost 		  MonetaryType not null,
	charges  	  MonetaryType not null,
	primary key (VIN)
);

-- USEDCAR

create table UsedCar (
	VIN  		 VINType references Car(VIN),
	plateNumber  varchar(6) not null,
	primary key (VIN)
);

-- Repair Job

create table RepairJob (
	VIN			 VINType,
	"number"  	 integer  constraint ValidNumber check ("number" >= 1 and "number" <= 999),
	description  varchar(250) not null,
	parts  		 MonetaryType not null,
	work 		 MonetaryType not null,
	"date"  	 date not null,
	CID 		 serial not null,					-- the job paid by client, total participation
	primary key (VIN, "number"),
	foreign key (VIN) references UsedCar(VIN),
	foreign key (CID) references Client(CID)
);

create table Does (
	EID			 serial,
	VIN			 VINType,
	"number"  	 integer  constraint ValidNumber check ("number" >= 1 and "number" <= 999),
	primary key (EID, VIN, "number"),
	foreign key (EID) references Mechanic(EID),
	foreign key (VIN, "number") references RepairJob(VIN, "number")

);

create table Buys (
	VIN  		 VINType,
	CID 	  	 serial,							-- seller
	EID		 	 serial not null,
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	primary key (CID, VIN, "date"),					-- assuming the same client may buy the same car mutiple times (e.g. buy -> sell -> buy back), 
													-- but we only allow the same client to perform this action once a day with the same car
	foreign key (CID) references Client(CID),
	foreign key (VIN) references Car(VIN),
	foreign key (EID) references Salesman(EID)
	

);

create table Sells (
	VIN  		 VINType,
	CID 	  	 serial,							-- buyer
	EID 	 	 serial not null,
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	primary key (CID, VIN, "date"),					-- assuming the same client may sell the same car mutiple times (e.g. sell -> buy -> sell out), 
													-- but we only allow the same client to perform this action once a day with the same car
	foreign key (CID) references Client(CID),
	foreign key (VIN) references Car(VIN),
	foreign key (EID) references Salesman(EID)

);

create table SellsNew (

	VIN  		 VINType,
	CID 	  	 serial,							-- buyer
	EID 	 	 serial not null,
	"date"	 	 date not null,
	price 	  	 MonetaryType not null,
	commission 	 MonetaryType not null,
	plateNumber  varchar(6) not null,
	primary key (CID, VIN),							-- once the car is sold, any selling action with the same car is treated as 2nd hand,
													-- hence, no need for adding "date" as part of the PK
	foreign key (CID) references Client(CID),
	foreign key (VIN) references Car(VIN),
	foreign key (EID) references Salesman(EID)

);