DROP TABLE student;
DROP TABLE imported;

-- Create a simple student table
CREATE TABLE student
(
	studentID INT PRIMARY KEY,
	firstname CHAR(20),
    lastname CHAR(30),
    address CHAR(50),
    city CHAR(30),
    state CHAR(2),
    zip CHAR(5)
);

-- Create a simple employees table
CREATE TABLE imported
(
	studentID INT PRIMARY KEY,
	firstname CHAR(20),
    lastname CHAR(30),
    address CHAR(50),
    city CHAR(30),
    state CHAR(2),
    zip CHAR(5)
);

-- populate student table with students 
INSERT INTO student (studentID, firstname, lastname, address, city, state, zip) VALUES
	(1, 'Lara', 'Garcia', '850 Shady Beach Ave', 'Stockholm', 'NJ', '07460'),
	(2, 'Pola', 'Hayek', '430 Brial Hwy', 'Paterson', 'NJ', '07513'),
	(3, 'Martin', 'Bryan', '1199 Baum Ln', 'Hawthorne', 'NJ', '07506'),
	(4, 'Hiroshi', 'Tanaka', '2152 Kylie Pl','Pompton Lakes', 'NJ', '07442'),
	(5, 'Yoshio', 'Ito', '211 Cameron Rd', 'Ringwood','NJ','07456')
	;

-- two new students (#6 and #7)
-- Lara Garcia (#1) changed her last name
-- Pola Hayek (#2) changed address
INSERT INTO imported (studentID, firstname, lastname, address, city, state, zip) VALUES
	(1, 'Lara', 'Mueller', '850 Shady Beach Ave', 'Stockholm', 'NJ', '07460'),
	(2, 'Pola', 'Hayek', '745 Merle Blvd', 'Clifton', 'NJ', '07014'),
	(6, 'Juvina', 'Pawar', '153 Surrey Rd', 'Hawthorne', 'NJ', '07507'),
	(7, 'Li', 'Gao', '1303 Lakina Ln', 'Totowa', 'NJ', '07511')
	;

-- Start the merge; specify primary key
MERGE student 
    USING imported 
    ON imported.studentid = student.studentid

    -- For updated records (found in both tables), perform an UPDATE query
    WHEN MATCHED THEN UPDATE 
    SET
        studentID = imported.studentID,
        firstname = imported.firstname,
        lastname = imported.lastname, 
        address = imported.address, 
        city = imported.city,
        state = imported.state,
        zip = imported.zip

   -- For records found in the imported table, but not student, do an INSERT
   -- "TARGET" refers to the main table; in our case, student
    WHEN NOT MATCHED BY TARGET THEN
    INSERT (studentID, firstname, lastname, address, city, state, zip) VALUES 
    (imported.studentID, imported.firstname, imported.lastname, imported.address, imported.city, imported.state, imported.zip)

    -- Could also do something if there are records in the old data set that do not
    -- appear in the new data set. If you uncomment the following lines, it would delete
    -- students 3, 4, and 5 as they do not appear in the imported table.
    -- "SOURCE" refers to the imported table
    --WHEN NOT MATCHED BY SOURCE THEN
    --DELETE 
;

-- Can view merged table here:
SELECT *
FROM student;

-- can probably safely drop the imported table now
DROP table imported;
