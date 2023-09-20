--select * from pg_catalog.pg_views where schemaname='BUILDER';
commit;
drop view if exists a;
drop view if exists b;
drop view if exists w7a;
drop view if exists w7b;
drop view if exists w7c;
-- drop bottom layer
--
DROP TABLE  if exists B2_CORDERLINE;
DROP TABLE  if exists B2_SORDERLINE;
--
-- drop second layer
--
DROP TABLE  if exists B2_CORDER;
DROP TABLE  if exists B2_SORDER;
DROP TABLE  if exists B2_STOCK;
--
-- Drop top layer
--
DROP TABLE  if exists B2_SUPPLIER;
DROP TABLE  if exists B2_CUSTOMER;
DROP TABLE  if exists B2_STAFF;
--
-- Create first layer of tables - no dependencies
--
CREATE TABLE B2_CUSTOMER (
	Customer_Id       SERIAL PRIMARY KEY,
	Customer_Name      VARCHAR(25) not null,
	Customer_Address   VARCHAR(80)
);


CREATE TABLE B2_SUPPLIER (
	Supplier_Id       serial     PRIMARY KEY,
	Supplier_Name      varchar(25) not null,
	Supplier_Address   varchar(80) not null,
	Amount_Owed        numeric(10,2)
);

CREATE TABLE B2_STAFF (
	Staff_no           serial     PRIMARY KEY,
	Staff_name 	   varchar(20) not null,
	Staff_role 	   varchar(10),
	Reports_to 	   integer    REFERENCES B2_STAFF(staff_no)
);

--
-- Create second layer of tables - dependent on the first layer
--
CREATE TABLE B2_STOCK (
	Stock_Code        CHAR(5)   PRIMARY KEY,
	Stock_Description varchar(20) not null,
	Unit_Price        numeric(10,2) not null,
	UnitCostPrice     numeric(10,2) not null,
	Stock_level       numeric(7) not null,
	Reorder_level     numeric(7),
	Supplier_Id       integer     REFERENCES B2_SUPPLIER not null
);

CREATE TABLE B2_CORDER (
	corderno          serial   PRIMARY KEY,
	Order_Date        DATE default current_date not null ,
	Customer_Id       integer    REFERENCES B2_CUSTOMER not null,
	StaffPaid         integer    REFERENCES B2_STAFF(staff_no) not null,
	StaffIssued       integer    REFERENCES B2_STAFF(staff_no)
);


CREATE TABLE B2_SORDER (
	SOrderNo   serial    PRIMARY KEY,
	SOrderDate DATE default current_date not null,
	DeliveredDate     DATE         NULL,
	Supplier_Id integer          REFERENCES B2_SUPPLIER not null,
CONSTRAINT DATECHECK CHECK(DELIVEREDDATE >SORDERDATE)
);
--
-- Create third layer - dependent on the second layer.
--
CREATE TABLE B2_CORDERLINE (
	Corderno        integer   REFERENCES B2_CORDER,
	Stock_Code        CHAR(5)  REFERENCES B2_STOCK,
	QuantityRequired  numeric(8),
	PRIMARY KEY (COrderno,stock_code)
);

CREATE TABLE B2_SORDERLINE (
	SOrderNo          integer   REFERENCES B2_SORDER not null,
	Stock_Code        CHAR(5)  REFERENCES B2_STOCK not null,
	StockRequired     numeric(8),
	PRIMARY KEY  (SOrderNo,Stock_Code)
);
--
--DROP TABLE LOG_TABLE;
--DROP TABLE RESTOCK;
----
--  CREATE TABLE ERRORLOG 
--   (	TABNAM varchar(20), 
--	OP varchar(3), 
--	OPUSER varchar(20), 
--	OPDATE DATE, 
--	MSG varchar(200)
--   ) ;
-- 
-- 
--  CREATE TABLE LOG_TABLE 
--   (	OP CHAR(3) DEFAULT 'INS' NOT NULL , 
--	TABNAM varchar(15) NOT NULL , 
--	PRIMKEY varchar(10) NOT NULL , 
--	LOGDATE DATE DEFAULT current_date, 
--	LOGUSER varchar(20), 
--	 CHECK (op in ('INS','UPD','DEL')) );
-- 
--  CREATE TABLE RESTOCK 
--   (	RESTOCKDATE DATE, 
--	SCODE CHAR(5)
--   );
 --
begin transaction;
-- Layer 1 Customer - B2_STAFF - B2_SUPPLIER
INSERT INTO B2_CUSTOMER(CUSTOMER_NAME, CUSTOMER_ADDRESS) VALUES 
('John Flaherty','23 The Green, Blackhill, Dublin 25.'),
( 'Gerard Temple','9 Genview Tce, Limerick'),
( 'John Browne','2 Kevin St., Dublin 8'),
( 'Aidan Bourke','64 Earlsfort Court, Dublin 8'),
( 'Mary Martin','33 The Lawn, Greenhills, Dublin 22'),
( 'Nick Knowles','Television land'),
( 'Tim Taylor','34 Greygates, Mt. Merrion');
--
--select * from b2_customer;
--/*
--
INSERT INTO B2_STAFF(STAFF_NAME,STAFF_ROLE) VALUES 
( 'Joe Owner','Owner');

INSERT INTO B2_STAFF(STAFF_NAME,STAFF_ROLE,REPORTS_TO) VALUES 
('Fred Flinstone','Foreman',1),
('Robbie Redstone','Sales',1),
('Paul Moran','Foreman',2),
('Mick O''Donnell','Sales',3);
--
--
--
INSERT INTO B2_SUPPLIER (SUPPLIER_NAME, SUPPLIER_ADDRESS, AMOUNT_OWED) VALUES 
('Buckleys','Quarry town, Quarrysville, D44.',6999.5),
('Brendan Moore','44 Kevin St., D8',4444), 
('James McGovern','33 Synge St.',4443),
('Liam Keenan','33 Mount Vernon Ave',8888),
('Mary O''Dwyer','Appian Way, D2',33333), 
('Oliver Moore','Georges St., D2',3321),
('Robert O''Mahony','Fitzwilliam Sq',2222),
('Paula O''Brien','21 Liberty Lane, D8',3000),
('June Browne','33 Liberty Lane',4000),
('Paul Sloan','44 Liberty Lane',30000),
('Kevin Kelly','33 Bride St, D8',4444);
--SELECT * FROM B2_SUPPLIER;
--
--  Layer 2 - Stock - Sorder - B2_CORDER
--
INSERT INTO B2_STOCK VALUES ('BRK11', 'Brick - red, 30x100',2.5,1.5,750,100,1),
('A101', 'Cavity blocks(100)',200,210,300,100,1),
('A111', 'Red bricks(100)',200,250,294,100,1),
('B101', '2"x4" lengths',9.5,7,40,45,4),
('B111', 'Window Frames 2''x4''',45,38,10,5,8),
('C101', '6" Nails(50)',5.95,5,30,25,10),
('C121', '6" Nails(100)',9.95,8,20,25,10),
('D101', 'Workbench',250,200,138,1,11),
('D131', 'cordless Drill',200,150,30,10,6),
('E101', 'Cavity blocks(500)',1000,500,172,200,1),
('E141', 'Cavity blocks(200)',400,130,300,200,1),
('A642', '4"x4" treated timber',9.5,8,20,5,10),
('J555', 'Box of 6" screws',5,4,100,10,8),
('J501', 'Phillips screwdriver',8,6,38,10,5),
('B141', 'U-lock bicycle lock', 19.99,15,40,10,10),
('B142', 'Unicycle', 500,499.99,5,1,10);
--
-- PLACE AN ORDER WITH EACH SUPPLIER
/*
 * SELECT SUPPLIER_ID FROM B2_SUPPLIER except
SELECT SUPPLIER_ID FROM B2_SUPPLIER WHERE SUPPLIER_ID NOT IN (SELECT SUPPLIER_ID FROM B2_STOCK);
--
-- SUPPLIERS ARE 1, 4, 5, 6, 8, 10 AND 11.
*/

INSERT INTO B2_SORDER (SORDERDATE, SUPPLIER_ID) VALUES 
(current_date, 4),
(current_date-5, 1),
(current_date-10, 5),
(current_date-5, 10),
(current_date, 11);--713
INSERT INTO B2_SORDER (SORDERDATE,DELIVEREDDATE, SUPPLIER_ID) VALUES 
(current_date-500, current_date-480, 1),
(current_date-50, current_date-48, 4),
(current_date-5, current_date-4, 4),
(current_date-50, current_date-48, 5),
(current_date-5, current_date-4, 6),
(current_date-500, current_date-480, 6),
(current_date-50, current_date-48, 8),
(current_date-5, current_date-4, 8),
('01-Jan-2015', '01-Mar-2015',1);
--SELECT * FROM B2_SUPPLIER;
--SELECT * FROM B2_SORDER;

----
/*SELECT * FROM B2_SORDER;*/
--
-- B2_SORDERLINE - 
--
--SELECT STOCK_CODE FROM B2_STOCK WHERE SUPPLIER_ID = 1;
--SELECT * FROM B2_SORDERLINE;
--  1 SUPPLIER ORDERS
INSERT INTO B2_SORDERLINE VALUES 
(2,'BRK11', 18),         
(2,'A101', 14),       
(2,'E101', 27),    
(2,'A111', 5),           
(2,'E141', 1),
(3,'BRK11', 5),        
(3,'A101', 4),      
(3,'E101', 10),     
(3,'A111', 14),           
(3,'E141', 1),
(4,'B101', 24),
(5,'B101', 18),
(6 ,'J501', 12), 
(5,'J501', 2),
(5,'D131', 5); 
--SELECT * FROM B2_SORDERLINE;
--SELECT * FROM B2_SORDER;
--SELECT STOCK_CODE FROM B2_STOCK WHERE SUPPLIER_ID = 11;
--  6 SUPPLIER ORDERS
INSERT INTO B2_SORDERLINE VALUES 
(14-3,'B111',10), 
(14-3,'J555',20),  
(14-2,'J555', 3),          
(14-1,'C101', 3),           
(14-1,'C121', 3),           
(14-1,'A642', 3),           
(14-1,'B141', 3),           
(14-1,'B142', 3),         
(12,'D101', 3),
(14, 'E101', 4);
--select * from b2_sorderline;
--
--SELECT * FROM B2_CORDER;
--SELECT * FROM B2_CUSTOMER;
/*
SELECT * FROM B2_SORDERLINE;*/
INSERT INTO B2_CORDER(ORDER_DATE, CUSTOMER_ID, STAFFPAID, STAFFISSUED) VALUES 
(current_date-500,7-6,3,2),
(current_date-580,5,1,2),
(current_date-504,5,3,4),
(current_date-500,7-1,5,1),
(current_date-500,7-6,3,4),
(current_date-500,7-6,1,4),
(current_date-500,7-3,3,1);
INSERT INTO B2_CORDER (ORDER_DATE, CUSTOMER_ID, STAFFPAID) VALUES 
(current_date-2,7-1,3),
(current_date-8,7-6,5);
--
--  Layer 3 - B2_CORDERLINE, B2_SORDERLINE
--SELECT * fROM B2_CORDER;
--SELECT * FROM B2_cORDERLINE;
INSERT INTO B2_CORDERLINE VALUES 
(9-8,'A101', 1),
(9-8,'A111', 2),
(9-8,'A642', 3),           
(9-8,'B101', 3),           
(9-4,'B111', 1),           
(9-4,'B141', 2),           
(9-4,'BRK11', 1),          
(9-4,'C101', 2),          
(9-3,'C121', 1),           
(9-3,'D101', 2),           
(9-3,'D131', 1),           
(9,'E101', 2),         
(9,'E141', 1),           
(9,'J501', 2),           
(9,'J555', 1), 
(9-7,'E101', 2),           
(9-1,'E141', 2),           
(9-2,'J501', 1),           
(9-5,'J555', 1);
--

COMMIT;*/
/*select stock_code,stock_level, stockrequired from b2_stock join b2_sorderline using (stock_code);
select stock_code from b2_stock bs
except
select stock_code from b2_sorderline;
select stock_code from b2_sorderline bs
except
select stock_code from b2_stock;
select distinct stock_code from b2_sorderline;

select distinct stock_code from b2_corderline;


select */