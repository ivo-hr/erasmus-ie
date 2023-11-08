-- 1. Create a role called bespoke_computers with login and password besp0ke
CREATE ROLE bespoke_computers with login password 'besp0ke';
CREATE SCHEMA AUTHORIZATION bespoke_computers;
GRANT ALL ON ALL TABLES IN SCHEMA bespoke_computers TO bespoke_computers;

-- 2. Login into bespoke_computers to create tables
-- 3. Create tables
drop table if exists componentdetail;
drop table if exists component;
drop table if exists supplier;
drop table if exists computer;
drop table if exists "order";
drop table if exists customer;


CREATE TABLE customer (
    customer_id         SERIAL PRIMARY KEY,
    customer_name       VARCHAR(255) NOT NULL,
    customer_address    VARCHAR(255) NOT NULL,
    contact_number      VARCHAR(20) NOT NULL,
    email               VARCHAR(255) NOT NULL
);

CREATE TABLE "order" (
    order_id        SERIAL PRIMARY KEY,
    customer_id     INTEGER NOT NULL,
    order_date      DATE NOT NULL,
    shipped_date    DATE,
    status          VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

CREATE TABLE computer (
    computer_id     VARCHAR(255) PRIMARY KEY,
    order_id        INTEGER NOT NULL,
    status          VARCHAR(255),
    FOREIGN KEY (order_id) REFERENCES "order" (order_id)
);

CREATE TABLE supplier (
    supplier_id         SERIAL PRIMARY KEY,
    supplier_name       VARCHAR(255) NOT NULL,
    supplier_address    VARCHAR(255) NOT NULL,
    supplier_phone      VARCHAR(255) NOT NULL
);

CREATE TABLE component (
    component_id            SERIAL PRIMARY KEY,
    computer_id             VARCHAR(255) NOT NULL,
    supplier_id             INTEGER NOT NULL,
    FOREIGN KEY (computer_id) REFERENCES computer (computer_id),
    FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id)
);

CREATE TABLE componentdetail (
    component_id            INTEGER PRIMARY KEY,
    component_description   VARCHAR(255) NOT NULL,
    component_type          VARCHAR(255) NOT NULL,
    serial_no               VARCHAR(255) NOT NULL,
    FOREIGN KEY (component_id) REFERENCES component (component_id)
);


-- 4. Populate the tables with data

INSERT INTO customer (customer_id, customer_name, customer_address, contact_number, email)
VALUES (3, 'John Doe', '123 Main Street', '+1234567890', 'john.smith@example.com');
INSERT INTO customer (customer_id, customer_name, customer_address, contact_number, email)
VALUES (4, 'Alice Johnson', '456 Elm Street', '+9876543210', 'alice.johnson@example.com');
INSERT INTO customer (customer_id, customer_name, customer_address, contact_number, email)
VALUES (6, 'Bob Smith', '789 Oak Lane', '+1234567890', 'bob.smith@example.com');
INSERT INTO customer (customer_id, customer_name, customer_address, contact_number, email)
VALUES (7, 'Emily White', '789 Willow Lane', '+4445556666', 'emily.white@example.com');


INSERT INTO "order" (order_id, customer_id, order_date, shipped_date, status)
VALUES (4, 4, '2023-10-25', '2023-10-31', 'Open');
INSERT INTO "order" (order_id, customer_id, order_date, shipped_date, status)
VALUES (3, 3, '2023-10-25', '2023-10-31', 'In Progress');
INSERT INTO "order" (order_id, customer_id, order_date, shipped_date, status)
VALUES (6, 6, '2023-10-25', '2023-10-31', 'Shipped');
INSERT INTO "order" (order_id, customer_id, order_date, shipped_date, status)
VALUES (10, 7, '2023-10-25', '2023-10-31', 'Open');


INSERT INTO computer (computer_id, order_id, status)
VALUES ('#99101112', 4, 'In Assembly');
INSERT INTO computer (computer_id, order_id, status)
VALUES ('#11223344', 3, 'In Assembly');
INSERT INTO computer (computer_id, order_id, status)
VALUES ('#98765432', 6, 'Ready for Shipping');
INSERT INTO computer (computer_id, order_id, status)
VALUES ('#2346783', 10, 'Completed');


INSERT INTO supplier (supplier_id, supplier_name, supplier_address, supplier_phone)
VALUES (9910, 'Corsair', '456 Supplier Lane', '555-555-5557');
INSERT INTO supplier (supplier_id, supplier_name, supplier_address, supplier_phone)
VALUES (1234, 'AMD', '321 Supplier Lane', '555-555-5556');
INSERT INTO supplier (supplier_id, supplier_name, supplier_address, supplier_phone)
VALUES (5432, 'Samsung', '789 Supplier Drive', '333-333-4444');
INSERT INTO supplier (supplier_id, supplier_name, supplier_address, supplier_phone)
VALUES (2314, 'Western Digital', '789 Storage Drive', '333-333-3333');

INSERT INTO component (component_id, computer_id, supplier_id)
VALUES (7, '#99101112', 9910);
INSERT INTO component (component_id, computer_id, supplier_id)
VALUES (6, '#11223344', 1234);
INSERT INTO component (component_id, computer_id, supplier_id)
VALUES (8, '#98765432', 5432);
INSERT INTO component (component_id, computer_id, supplier_id)
VALUES (9, '#2346783', 2314);

INSERT INTO componentdetail (component_id, component_description, component_type, serial_no)
VALUES (7, 'Energy', 'Power Supply', 'C650');
INSERT INTO componentdetail (component_id, component_description, component_type, serial_no)
VALUES (6, 'Central Processing Unit', 'CPU Processor', 'AMD-r-5-3600');
INSERT INTO componentdetail (component_id, component_description, component_type, serial_no)
VALUES (8, 'Graphical Processing Unit', 'GPU Processor', 'GF55');
INSERT INTO componentdetail (component_id, component_description, component_type, serial_no)
VALUES (9, 'Primary Memory Storage', 'Storage Device', 'WD40G');

-- Until now we have created the tables and populated them with data.
-- Now we will proceed to create a supply manager role with specific permissions to access and modify the supplier table.
-- 5. Create a new role called supply_manager with login and password besp0ke_sm

CREATE ROLE supply_manager with login password 'besp0ke_sm';
GRANT USAGE ON SCHEMA bespoke_computers TO supply_manager;
ALTER ROLE supply_manager SET search_path TO bespoke_computers;
GRANT SELECT ON bespoke_computers.supplier to supply_manager;
GRANT UPDATE ON bespoke_computers.supplier to supply_manager;
GRANT INSERT ON bespoke_computers.supplier to supply_manager;

-- 6. Login into supply_manager to test the permissions

-- This should return the supplier table
SELECT * FROM supplier;

-- This will return an error due to the lack of permissions
SELECT * FROM computer;