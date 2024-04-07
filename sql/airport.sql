use bernard;

BEGIN TRANSACTION;
create table passenger(
	id int primary key identity(1,1),
	name varchar(50) not null,
	email varchar(150) not null check(email like '%@%'),
	password varchar(255) not null,
	phone_num varchar(15) not null,
	pin varchar(11) not null check(pin like '%/%') unique
);

create table pilot(
	id int primary key identity(1,1),
	name varchar(50) not null,
	age int not null check(age > 28),
	email varchar(150) not null check(email like '%@%'),
	phone_num varchar(15) not null
);

create table plane(
	id int primary key identity(1,1),
	name varchar(100) not null,
	type varchar(100) not null check(type in ('private', 'public')), 
	capacity int not null check(capacity > 0),
	active char(1) not null
);


create table destination(
	id int primary key identity(1,1),
	country varchar(50) not null,
	capital varchar(50) not null,
	avg_temp float not null
);


create table flight(
	id int primary key identity(1,1),
	fly_number int not null check(fly_number > 0) unique,
	destination_id int foreign key references destination(id),
	plane_id int foreign key references plane(id),
	pilot_id int foreign key references pilot(id),
	date_leaving date not null,
	date_arriving date not null,
	price int not null check(price > 0)
);


create table reservation(
	id int primary key identity(1,1),
	pin int not null check(pin > 0) unique,
	passenger_id int foreign key references passenger(id),
	flight_id int foreign key references flight(id),
	date datetime not null,
	price int not null check(price > 0)
);



/* views*/
create view print_all_passengers
as
select passenger.name, passenger.email, passenger.phone_num, passenger.pin
from passenger;

create view print_all_pilots
as
select pilot.name, pilot.age, pilot.email, pilot.phone_num
from pilot;

create view print_all_planes
as
select plane.name, plane.type, plane.capacity, plane.active
from plane;

create view print_all_destinations
as
select destination.country, destination.capital, destination.avg_temp
from destination;

create view print_all_flights
as
select flight.fly_number, destination.country, plane.name as plane_name, pilot.name as pilot_name, flight.date_leaving, flight.date_arriving, flight.price
from flight join destination on flight.destination_id = destination.id join plane on flight.plane_id = plane.id join pilot on flight.pilot_id = pilot.id;

create view print_all_reservations
as
select reservation.pin as pin, flight.fly_number as fly_number, passenger.name as passenger, destination.country as country, plane.name as plane, pilot.name as pilot, flight.date_leaving, flight.date_arriving, reservation.price as price
from reservation inner join passenger ON reservation.passenger_id = passenger.id inner join flight ON reservation.flight_id = flight.id inner join destination ON flight.destination_id = destination.id inner join plane ON flight.plane_id = plane.id inner join pilot ON flight.pilot_id = pilot.id;
COMMIT	

	insert into passenger(name, email, password, phone_num, pin) values('Karel', 'kaja@gmail.com', '99763235b36a8ca5275181f7428b88ba01760ef610e555f01dac4264ad56e0f4', '777666555', '010203/4748');
	delete from passenger;