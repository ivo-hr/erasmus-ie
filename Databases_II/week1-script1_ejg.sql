--a

SELECT
    s.Stock_Code,
    s.Stock_Description,
    SUM(sl.StockRequired * s.Unit_Price) AS TotalSalesRevenue,
    SUM(sl.StockRequired * s.UnitCostPrice) AS TotalCostPrice,
    SUM(sl.StockRequired * s.Unit_Price) - SUM(sl.StockRequired * s.UnitCostPrice) AS Profit
FROM
    B2_STOCK s
JOIN
    B2_SORDERLINE sl ON s.Stock_Code = sl.Stock_Code
GROUP BY
    s.Stock_Code, s.Stock_Description
HAVING
    SUM(sl.StockRequired * s.Unit_Price) - SUM(sl.StockRequired * s.UnitCostPrice) > 0;
   
--b
SELECT Supplier_Name
FROM B2_SUPPLIER
WHERE Supplier_Id NOT IN (SELECT DISTINCT Supplier_Id FROM B2_STOCK);

--c
SELECT c.Customer_Name
FROM B2_CUSTOMER c
JOIN B2_CORDER co ON c.Customer_Id = co.Customer_Id
JOIN B2_CORDERLINE col ON co.corderno = col.Corderno
JOIN B2_STOCK s ON col.Stock_Code = s.Stock_Code
WHERE s.Stock_Description = 'Phillips screwdriver';

--d
SELECT DISTINCT c.Customer_Name
FROM B2_CUSTOMER c
JOIN B2_CORDER co ON c.Customer_Id = co.Customer_Id
JOIN B2_CORDERLINE col ON co.corderno = col.Corderno
JOIN B2_STOCK s ON col.Stock_Code = s.Stock_Code
WHERE s.Stock_Description IN ('Phillips screwdriver', 'Box of 6" screws');

--e
SELECT c.Customer_Name
FROM B2_CUSTOMER c
JOIN B2_CORDER co ON c.Customer_Id = co.Customer_Id
JOIN B2_CORDERLINE col ON co.corderno = col.Corderno
JOIN B2_STOCK s ON col.Stock_Code = s.Stock_Code
WHERE s.Stock_Description IN ('Phillips screwdriver', 'Box of 6" screws')
GROUP BY c.Customer_Name
HAVING COUNT(DISTINCT s.Stock_Description) = 2;

--f
SELECT DISTINCT s.Staff_name
FROM B2_STAFF s
JOIN B2_CORDER co ON s.Staff_no =co.staffissued 
JOIN B2_CORDERLINE col ON co.corderno = col.cOrderNo
JOIN B2_STOCK st ON col.Stock_Code = st.Stock_Code
JOIN B2_SUPPLIER sup ON st.Supplier_Id = sup.Supplier_Id
WHERE sup.Supplier_Name = 'Paul Sloan';
