DROP TABLE customers;

-- Create a simple customers table
CREATE TABLE customers
(
	customerid INT PRIMARY KEY,
	name CHAR(10)
);

-- populate with customers with various CustomerID lengths
INSERT INTO customers (customerid, name) VALUES
	(1,'Oney'),
	(22,'Twoey'),
	(333,'Threey'),
	(4444,'Foury'),
	(55555,'Fivey')
	;

SELECT * FROM customers;

SELECT 'C'+ CASE
	WHEN LEN(customerid)=1
		THEN '0000'+ CAST(customerid AS CHAR(1))
	WHEN LEN(customerid)=2
		THEN '000'+ CAST(customerid AS CHAR(2))
	WHEN LEN(customerid)=3
		THEN '00'+ CAST(customerid AS CHAR(3))
	WHEN LEN(customerid)=4
		THEN '0'+ CAST(customerid AS CHAR(4))
	WHEN LEN(customerid )=5
		THEN CAST(customerid AS CHAR(5))
	END AS newid
FROM customers;

SELECT 'C'+ CASE
	WHEN LEN(customerid)=1
		THEN '0000'
	WHEN LEN(customerid)=2
		THEN '000'
	WHEN LEN(customerid)=3
		THEN '00'
	WHEN LEN(customerid)=4
		THEN '0'
	END + CAST(customerid as VARCHAR) AS newid
FROM customers;


-- Note: SUBSTRING uses "1" as the first character, 2 is the second character
SELECT 'C'+SUBSTRING(CAST(customerid+100000 AS CHAR(6)),2,6) AS newid
FROM customers;


SELECT 'C'+REPLICATE('0',5-LEN(CAST(customerid AS VARCHAR))) + CAST(customerid AS VARCHAR)
FROM customers;


SELECT FORMAT(customerid, 'C0000#')
FROM Customers;
