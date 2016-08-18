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
    FirstName	 varchar(50) not null,
    LastName 	 varchar(50) not null,
    Salary       integer not null check (Salary > 0),
    TFN			 integer(9) not null,
	primary key (EID)
);

create table Admin (
	EID			serial references Employee(EID),
	primary key (EID)

);

create table Mechanic (
	EID			serial references Employee(EID),
	License 	char(8) not null,
	primary key (EID)
);

create table Salesman (
	EID			serial references Employee(EID),
	CommRate 	integer not null constraint ValidCommRate check (CommRate >= 5 and CommRate <= 20),
	primary key (EID) 	
);

-- CLIENT

create table Client (
	CID          serial,
	Name 		 varchar(100),
	Address  	 varchar(200),
	Phone 		 PhoneType,
	Email 		 EmailType,
	primary key (CID)
);

create table Company (
	CID 		 serial references Client(CID),
	URL 		 URLType,
	ABN  		 integer(11),
	primary key (CID)
);


-- CAR

create domain CarLicenseType as
        char(6) check (value ~ '[0-9A-Za-z]{6}');

create domain OptionType as varchar(12)
	check (value in ('sunroof','moonroof','GPS','alloy wheels','leather'));

create domain VINType as char(17) check (value ~ '[^IOQ]')

create table Car (
	VIN 		 VINType,
	Manufacturer varchar(40) not null,
	Model 		 varchar(40) not null,
	Year		 integer not null,
	primary key (VIN)
);

-- Options

create table Options (
	VIN 		 VINType references Car(VIN),
	Options      OptionType,
	primary key (VIN, Options),
	foreign key (VIN)
);

create table NewCar (
	VIN 		 VINType references Car(VIN),
	Cost 		 text not null,
	Charges  	 text not null,
	SellsNew	 serial references Salesman(EID),
	"Date"	 	 date,
	Price 	  	 text,
	Commission 	 text,
	Client 	  	 serial references Client(CID),
	PlateNumber  varchar(6) not null,
	primary key (VIN),
	foreign key (SellsNew),
	foreign key (Client)
);

create table UsedCar (
	VIN  		 VINType references Car(VIN),
	PlateNumber  varchar(6) not null,
	Buys		 serial references Salesman(EID),
	Sells 	 	 serial references Salesman(EID),
	"Date"	 	 date,
	Price 	  	 text,
	Commission 	 text,
	Client 	  	 serial references Client(CID),
	primary key (VIN),
	foreign key (Buys),
	foreign key (Sells),
	foreign key (Client)
);

-- Repair Job

create table RepairJob (
	EID			serial references Mechanic(EID),
	"Number"  	integer,
	Description varchar(250),
	Parts  		text,
	Work 		text,
	"Date"  	date,
	Repairs 	VINType not null references UsedCar(VIN),
	PaidBy 		CID not null references Client(CID),
	primary key (EID, "Number"),
	foreign key (EID),
	foreign key (Repairs),
	foreign key (PaidBy)
);