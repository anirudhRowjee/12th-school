create table Tourist(
    Tcode int not null primary key,
    Name varchar(50) not null,
    Age int not null,
    Agency varchar(50) not null,
    Package_Amt int not null,
    Travel_Date date not null default '1900-01-01'
);    

insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (101, 'Raghavendra', 26, 'Cross Roads', 12000, '2010-01-23');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (102, 'Shazia', 32, 'Go Places', 10000, '2010-03-24');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (103, 'Hardeep', 30, 'Cross Roads', 8000, '2009-04-21');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (105, 'Lisa', 23, 'Cross Roads', 9000, '2009-07-18');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (108, 'Diana', 21, 'Go Places', 15000, '2010-03-11');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (109, 'Madhu', 23, 'Go Places', 15000, '2010-03-17');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (110, 'Srinivas', 30, 'Cross Roads', 2000, '2009-03-16');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (111, 'Medha', 29, 'Go Places', 16560, '2009-06-14');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (112, 'Uma', 33, 'Cross Roads', 20000, '2010-12-15');
insert into Tourist(Tcode, Name, Age, Agency, Package_Amt, Travel_Date) VALUES (113, 'Kavita', 34, 'Cross Roads', 21000, '2009-11-15');

create table Places (
    Pcode int primary key not null,
    Name varchar(30) not null,
    Tcode int not null,
    foreign key (Tcode) references Tourist(Tcode)
);

insert into Places(Pcode, Name, Tcode) VALUES (11, 'Agra', 101);
insert into Places(Pcode, Name, Tcode) VALUES (12, 'Jodhpur', 103);
insert into Places(Pcode, Name, Tcode) VALUES (13, 'Waynad', 105);
insert into Places(Pcode, Name, Tcode) VALUES (14, 'Alapuzha', 105);
insert into Places(Pcode, Name, Tcode) VALUES (15, 'Srinagar', 113);
insert into Places(Pcode, Name, Tcode) VALUES (16, 'Ajmer', 111);
insert into Places(Pcode, Name, Tcode) VALUES (17, 'Kanyakumari', 112);
insert into Places(Pcode, Name, Tcode) VALUES (18, 'Jharkhand', 110);

