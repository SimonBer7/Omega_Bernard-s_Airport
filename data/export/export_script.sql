USE [master]
GO
/****** Object:  Database [bernard]    Script Date: 21.04.2024 18:17:36 ******/
CREATE DATABASE [bernard]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'bernard', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS2019\MSSQL\DATA\bernard.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'bernard_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS2019\MSSQL\DATA\bernard_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [bernard] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [bernard].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [bernard] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [bernard] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [bernard] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [bernard] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [bernard] SET ARITHABORT OFF 
GO
ALTER DATABASE [bernard] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [bernard] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [bernard] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [bernard] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [bernard] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [bernard] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [bernard] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [bernard] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [bernard] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [bernard] SET  ENABLE_BROKER 
GO
ALTER DATABASE [bernard] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [bernard] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [bernard] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [bernard] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [bernard] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [bernard] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [bernard] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [bernard] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [bernard] SET  MULTI_USER 
GO
ALTER DATABASE [bernard] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [bernard] SET DB_CHAINING OFF 
GO
ALTER DATABASE [bernard] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [bernard] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [bernard] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [bernard] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [bernard] SET QUERY_STORE = OFF
GO
USE [bernard]
GO
/****** Object:  Table [dbo].[passenger]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[passenger](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](50) NOT NULL,
	[email] [varchar](150) NOT NULL,
	[password] [varchar](255) NOT NULL,
	[phone_num] [varchar](15) NOT NULL,
	[pin] [varchar](11) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[print_all_passengers]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[print_all_passengers]
as
select passenger.name, passenger.email, passenger.phone_num, passenger.pin
from passenger;
GO
/****** Object:  Table [dbo].[pilot]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pilot](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](50) NOT NULL,
	[age] [int] NOT NULL,
	[email] [varchar](150) NOT NULL,
	[phone_num] [varchar](15) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[print_all_pilots]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[print_all_pilots]
as
select pilot.name, pilot.age, pilot.email, pilot.phone_num
from pilot;
GO
/****** Object:  Table [dbo].[plane]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plane](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](100) NOT NULL,
	[type] [varchar](100) NOT NULL,
	[capacity] [int] NOT NULL,
	[active] [char](1) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[print_all_planes]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[print_all_planes]
as
select plane.name, plane.type, plane.capacity, plane.active
from plane;
GO
/****** Object:  Table [dbo].[destination]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[destination](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[country] [varchar](50) NOT NULL,
	[capital] [varchar](50) NOT NULL,
	[avg_temp] [float] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[print_all_destinations]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[print_all_destinations]
as
select destination.country, destination.capital, destination.avg_temp
from destination;
GO
/****** Object:  Table [dbo].[flight]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[flight](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[fly_number] [int] NOT NULL,
	[destination_id] [int] NULL,
	[plane_id] [int] NULL,
	[pilot_id] [int] NULL,
	[date_leaving] [date] NOT NULL,
	[date_arriving] [date] NOT NULL,
	[price] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[print_all_flights]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[print_all_flights]
as
select flight.fly_number, destination.country, plane.name as plane_name, pilot.name as pilot_name, flight.date_leaving, flight.date_arriving, flight.price
from flight join destination on flight.destination_id = destination.id join plane on flight.plane_id = plane.id join pilot on flight.pilot_id = pilot.id;
GO
/****** Object:  Table [dbo].[reservation]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[reservation](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[pin] [int] NOT NULL,
	[passenger_id] [int] NULL,
	[flight_id] [int] NULL,
	[date] [datetime] NOT NULL,
	[price] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[print_all_reservations]    Script Date: 21.04.2024 18:17:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[print_all_reservations]
as
select reservation.pin as pin, flight.fly_number as fly_number, passenger.name as passenger, destination.country as country, plane.name as plane, pilot.name as pilot, flight.date_leaving, flight.date_arriving, reservation.price as price
from reservation inner join passenger ON reservation.passenger_id = passenger.id inner join flight ON reservation.flight_id = flight.id inner join destination ON flight.destination_id = destination.id inner join plane ON flight.plane_id = plane.id inner join pilot ON flight.pilot_id = pilot.id;
GO
SET IDENTITY_INSERT [dbo].[destination] ON 
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (1, N'Spain', N'Madrid', 24.5)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (2, N'Greece', N'Athens', 23.4)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (3, N'Slovakia', N'Bratislava', 14.8)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (4, N'Germany', N'Berlin', 16.1)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (5, N'Italy', N'Rome', 21.7)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (6, N'Great Britain', N'London', 12.6)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (7, N'Iceland', N'Reykjavik', 15.2)
GO
INSERT [dbo].[destination] ([id], [country], [capital], [avg_temp]) VALUES (8, N'Norway', N'Oslo', 10.7)
GO
SET IDENTITY_INSERT [dbo].[destination] OFF
GO
SET IDENTITY_INSERT [dbo].[flight] ON 
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (1, 101, 1, 1, 1, CAST(N'2024-05-15' AS Date), CAST(N'2024-05-29' AS Date), 25000)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (2, 102, 3, 2, 2, CAST(N'2024-05-28' AS Date), CAST(N'2024-05-11' AS Date), 15000)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (3, 103, 2, 3, 3, CAST(N'2024-05-01' AS Date), CAST(N'2024-05-11' AS Date), 14800)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (4, 104, 7, 6, 8, CAST(N'2024-05-12' AS Date), CAST(N'2024-05-29' AS Date), 19990)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (5, 105, 6, 7, 5, CAST(N'2024-05-27' AS Date), CAST(N'2024-05-07' AS Date), 16800)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (6, 106, 5, 1, 4, CAST(N'2024-06-01' AS Date), CAST(N'2024-06-13' AS Date), 7500)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (7, 107, 4, 3, 6, CAST(N'2024-06-05' AS Date), CAST(N'2024-06-27' AS Date), 12700)
GO
INSERT [dbo].[flight] ([id], [fly_number], [destination_id], [plane_id], [pilot_id], [date_leaving], [date_arriving], [price]) VALUES (8, 108, 8, 2, 5, CAST(N'2024-06-02' AS Date), CAST(N'2024-06-30' AS Date), 22500)
GO
SET IDENTITY_INSERT [dbo].[flight] OFF
GO
SET IDENTITY_INSERT [dbo].[passenger] ON 
GO
INSERT [dbo].[passenger] ([id], [name], [email], [password], [phone_num], [pin]) VALUES (1, N'Admin', N'admin@gmail.com', N'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', N'111111111', N'111111/1111')
GO
SET IDENTITY_INSERT [dbo].[passenger] OFF
GO
SET IDENTITY_INSERT [dbo].[pilot] ON 
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (1, N'Karel', 35, N'karel.novak@gmail.com', N'608125235')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (2, N'Jakub', 30, N'jakub.zeleny@gmail.com', N'609500200')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (3, N'Eva', 31, N'eva.prochazkova@gmail.com', N'605789123')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (4, N'Martin', 40, N'martin.svoboda@gmail.com', N'602345678')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (5, N'Tereza', 29, N'terezak@email.com', N'604987654')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (6, N'Petr', 32, N'petr.jiracek@email.com', N'603112233')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (7, N'Veronika', 37, N'veronika.horakova@email.com', N'601998877')
GO
INSERT [dbo].[pilot] ([id], [name], [age], [email], [phone_num]) VALUES (8, N'David', 45, N'david.kolar@email.com', N'606665544')
GO
SET IDENTITY_INSERT [dbo].[pilot] OFF
GO
SET IDENTITY_INSERT [dbo].[plane] ON 
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (1, N'Airbus A320', N'public', 500, N'1')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (2, N'Boeing 707', N'public', 400, N'1')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (3, N'Boeing 777', N'public', 650, N'1')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (4, N'Antonov An-38', N'public', 245, N'0')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (5, N'Airbus A747', N'public', 570, N'0')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (6, N'Gulfstream G200', N'private', 50, N'1')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (7, N'Boeing 444', N'public', 120, N'1')
GO
INSERT [dbo].[plane] ([id], [name], [type], [capacity], [active]) VALUES (8, N'Airbus 111', N'public', 230, N'0')
GO
SET IDENTITY_INSERT [dbo].[plane] OFF
GO
/****** Object:  Index [UQ__flight__A36F3C3CC06720EE]    Script Date: 21.04.2024 18:17:38 ******/
ALTER TABLE [dbo].[flight] ADD UNIQUE NONCLUSTERED 
(
	[fly_number] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__passenge__DD37D92DFD8FD018]    Script Date: 21.04.2024 18:17:38 ******/
ALTER TABLE [dbo].[passenger] ADD UNIQUE NONCLUSTERED 
(
	[pin] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__reservat__DD37D92D9DD500BF]    Script Date: 21.04.2024 18:17:38 ******/
ALTER TABLE [dbo].[reservation] ADD UNIQUE NONCLUSTERED 
(
	[pin] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[flight]  WITH CHECK ADD FOREIGN KEY([destination_id])
REFERENCES [dbo].[destination] ([id])
GO
ALTER TABLE [dbo].[flight]  WITH CHECK ADD FOREIGN KEY([pilot_id])
REFERENCES [dbo].[pilot] ([id])
GO
ALTER TABLE [dbo].[flight]  WITH CHECK ADD FOREIGN KEY([plane_id])
REFERENCES [dbo].[plane] ([id])
GO
ALTER TABLE [dbo].[reservation]  WITH CHECK ADD FOREIGN KEY([flight_id])
REFERENCES [dbo].[flight] ([id])
GO
ALTER TABLE [dbo].[reservation]  WITH CHECK ADD FOREIGN KEY([passenger_id])
REFERENCES [dbo].[passenger] ([id])
GO
ALTER TABLE [dbo].[flight]  WITH CHECK ADD CHECK  (([fly_number]>(0)))
GO
ALTER TABLE [dbo].[flight]  WITH CHECK ADD CHECK  (([price]>(0)))
GO
ALTER TABLE [dbo].[passenger]  WITH CHECK ADD CHECK  (([email] like '%@%'))
GO
ALTER TABLE [dbo].[passenger]  WITH CHECK ADD CHECK  (([pin] like '%/%'))
GO
ALTER TABLE [dbo].[pilot]  WITH CHECK ADD CHECK  (([age]>(28)))
GO
ALTER TABLE [dbo].[pilot]  WITH CHECK ADD CHECK  (([email] like '%@%'))
GO
ALTER TABLE [dbo].[plane]  WITH CHECK ADD CHECK  (([capacity]>(0)))
GO
ALTER TABLE [dbo].[plane]  WITH CHECK ADD CHECK  (([type]='public' OR [type]='private'))
GO
ALTER TABLE [dbo].[reservation]  WITH CHECK ADD CHECK  (([price]>(0)))
GO
ALTER TABLE [dbo].[reservation]  WITH CHECK ADD CHECK  (([pin]>(0)))
GO
/****** Object:  StoredProcedure [dbo].[print_reservation_detail]    Script Date: 21.04.2024 18:17:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[print_reservation_detail]
    @passenger_id INT,
	@reservation_pin INT
AS
BEGIN
    SELECT 
        reservation.pin AS reservation_pin,
		passenger.name AS passenger_name,
        destination.country AS destination_country,
        destination.capital AS destination_capital,
        destination.avg_temp AS destination_avg_temp,
        plane.name AS plane_name,
        pilot.name AS pilot_name,
        flight.date_leaving AS date_leaving,
        flight.date_arriving AS date_arriving,
        reservation.date AS reservation_date,
		reservation.price as price
    FROM 
        reservation 
    INNER JOIN 
        flight ON reservation.flight_id = flight.id 
    INNER JOIN 
        destination ON flight.destination_id = destination.id 
    INNER JOIN 
        plane ON flight.plane_id = plane.id 
    INNER JOIN 
        pilot ON flight.pilot_id = pilot.id
    INNER JOIN
        passenger ON reservation.passenger_id = passenger.id
    WHERE 
        reservation.passenger_id = @passenger_id and reservation.pin = @reservation_pin;
END
GO
/****** Object:  StoredProcedure [dbo].[print_reservations]    Script Date: 21.04.2024 18:17:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[print_reservations]
    @passenger_id INT
AS
BEGIN
    SELECT 
        reservation.pin AS reservation_pin,
		passenger.name AS passenger_name,
        destination.country AS destination_country,
        destination.capital AS destination_capital,
        destination.avg_temp AS destination_avg_temp,
        plane.name AS plane_name,
        pilot.name AS pilot_name,
        flight.date_leaving AS date_leaving,
        flight.date_arriving AS date_arriving,
        reservation.date AS reservation_date,
		reservation.price as price
    FROM 
        reservation 
    INNER JOIN 
        flight ON reservation.flight_id = flight.id 
    INNER JOIN 
        destination ON flight.destination_id = destination.id 
    INNER JOIN 
        plane ON flight.plane_id = plane.id 
    INNER JOIN 
        pilot ON flight.pilot_id = pilot.id
    INNER JOIN
        passenger ON reservation.passenger_id = passenger.id
    WHERE 
        reservation.passenger_id = @passenger_id;
END
GO
/****** Object:  StoredProcedure [dbo].[print_user_flights]    Script Date: 21.04.2024 18:17:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create procedure [dbo].[print_user_flights] @pin varchar(11)
as
begin
select flight.fly_number as fly_number, destination.country as country, plane.name as plane, pilot.name as pilot, flight.date_leaving, flight.date_arriving, flight.price as price
from reservation inner join passenger ON reservation.passenger_id = passenger.id inner join flight ON reservation.flight_id = flight.id inner join destination ON flight.destination_id = destination.id inner join plane ON flight.plane_id = plane.id inner join pilot ON flight.pilot_id = pilot.id
where passenger.pin = @pin;
end
GO
USE [master]
GO
ALTER DATABASE [bernard] SET  READ_WRITE 
GO
