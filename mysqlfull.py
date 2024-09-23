import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*******",   #Replace with your MySQL Workbench Password.
    database="users"     
)
if connection.is_connected():
    print("MySQL Connected....")
else:
    print("MySQL not Connected....")

mycursor = connection.cursor()

#####-----CRUD FUNCTIONS-----

###-----CREATE TABLE-----
userss ="create table if not exists userss(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255),age int, email VARCHAR(255), department VARCHAR(255), salary DECIMAL(10, 2))"
mycursor = connection.cursor()
mycursor.execute(userss)

###Insert 25 userss data
query = "INSERT INTO userss (name, age, email, department, salary) VALUES (%s, %s, %s, %s, %s)"
userss = [
    ("Avi Negi", 19, "Avi@example.com", "IT", 90000.00),
    ("Jane Smith", 30, "jane.smith@example.com", "HR", 60000.00),
    ("Michael Johnson", 28, "michael.johnson@example.com", "Finance", 55000.00),
    ("Emily Davis", 35, "emily.davis@example.com", "Marketing", 62000.00),
    ("Chris Lee", 24, "chris.lee@example.com", "Operations", 48000.00),
    ("Anna Brown", 32, "anna.brown@example.com", "Legal", 59000.00),
    ("James White", 40, "james.white@example.com", "IT", 75000.00),
    ("Laura Green", 27, "laura.green@example.com", "Finance", 51000.00),
    ("David Miller", 22, "david.miller@example.com", "HR", 47000.00),
    ("Sophia Wilson", 29, "sophia.wilson@example.com", "Marketing", 53000.00),
    ("Andrew Moore", 33, "andrew.moore@example.com", "Operations", 61000.00),
on.commit()



###-----FILTER DATA-----
###-----(COMPARISION OPERATORS)-----
##Equal to(=)
query = "SELECT * FROM userss WHERE salary = 50000"
mycursor.execute(query)
print(mycursor.fetchall())
connection.commit()


##Not Equal to(!=)
query = "SELECT * FROM userss WHERE salary != 50000"
mycursor.execute(query)
print(mycursor.fetchall())
connection.commit()


##Greater than(>)
query = "SELECT * FROM userss WHERE age > 30"
mycursor.execute(query)
print(mycursor.fetchall())
connection.commit()


##Lesser than(<)
query = "SELECT * From userss WHERE age < 30"
mycursor.execute(query)
print(mycursor.fetchall())
connection.commit()


#Greater than Equal to(>=)
query = "SELECT * FROM userss WHERE age >= 30"
mycursor.execute(query)
print(mycursor.fetchall())
connection.commit()


##Lesser than Equal to(<=)
query = "SELECT * FROM userss WHERE age <= 30"
mycursor.execute(query)
print(mycursor.fetchall())
connection.commit()



###-----(LOGICAL OPERATORS)-----
##AND----Both the conditions need to be TRUE
andquery = "SELECT * FROM userss WHERE age <= 30 AND salary >= 50000"
mycursor.execute(andquery)
print(mycursor.fetchall())
connection.commit()


##OR----Any one condition is TRUE it will includes.
orquery = "SELECT * FROM userss WHERE age <= 30 OR salary >= 50000"
mycursor.execute(orquery)
print(mycursor.fetchall())
connection.commit()


##NOT----to exclude specific conditions.
notquery = "SELECT * FROM userss WHERE NOT age <= 30"
mycursor.execute(notquery)
print(mycursor.fetchall())
connection.commit()


##IN----is used to specify multiple values.
inquery = "SELECT * FROM userss WHERE age IN (19,24,30)"
mycursor.execute(inquery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()


##BETWEEN----is used to filter the result set within a specific range of values.
betweenquery = "SELECT * FROM userss WHERE age BETWEEN 19 AND 30"
mycursor.execute(betweenquery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()

#find name between a to b
betweenquery = "SELECT * FROM userss WHERE name BETWEEN 'a' AND 'b'"
mycursor.execute(betweenquery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()


##IS NULL----is used to filter the result set to include only rows where the specified column is NULL.
isnullquery = "SELECT * FROM userss WHERE name IS NULL"
mycursor.execute(isnullquery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()


##LIKE----is used to search for a specified pattern in a column.
likequery = "SELECT * FROM userss WHERE name LIKE '%a%'"
mycursor.execute(likequery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()


##NOTLIKE----NOT LIKE is used to filter out rows that do not match a specified pattern.
notlikequery = "SELECT * FROM userss WHERE name NOT LIKE 'n%'"
mycursor.execute(notlikequery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()


##LIMIT----return data based on limit.
limitquery = "SELECT * FROM userss ORDER BY salary DESC LIMIT 2"
mycursor.execute(limitquery)
print(mycursor.fetchall())
connection.commit()


##ALIASES---- aliases are temporary names given to table columns or tables in your query.
aliasquery = "SELECT name AS Uname, age AS Uage FROM userss"
mycursor.execute(aliasquery)
result = mycursor.fetchall()
for i in result:
    print(i)
connection.commit()



###-----AGGREGATION FUNCTIONS----
##SUM----is used to calculate the total of a numeric column.
sumquery = "SELECT SUM(salary) FROM userss"
mycursor.execute(sumquery)
print(mycursor.fetchall())
connection.commit()


##AVG----is used to calculate the average of a numeric column.
avgquery = "SELECT AVG(salary) FROM userss"
mycursor.execute(avgquery)
print(mycursor.fetchall())
connection.commit()


##COUNT----is used to return the number of rows that match a specified condition.
countquery = "SELECT COUNT(name) FROM userss"
mycursor.execute(countquery)
print(mycursor.fetchall())
connection.commit()


##MIN----to return the minimum values
minquery = "SELECT MIN(salary) FROM userss"
mycursor.execute(minquery)
print(mycursor.fetchall())
connection.commit()


##MAX----to return the maximum values
maxquery = "SELECT MAX(salary) FROM userss"
mycursor.execute(maxquery)
print(mycursor.fetchall())
connection.commit()


##GROUP BY----cobline multiple rows and use with COUNT, MAX, MIN, AVG, SUM
groupbyquery = "SELECT AVG(salary), name FROM userss GROUP BY name"
mycursor.execute(groupbyquery)
print(mycursor.fetchall())
connection.commit()


##HAVING----it will work where and order by, group by also check condition based on AVG, COUNT, SUM.
havingquery = "SELECT COUNT(name), department FROM userss GROUP BY department HAVING COUNT(name)"
mycursor.execute(havingquery)
print(mycursor.fetchall())
connection.commit()



###-----QUARYING DATA-----
##ORDER BY----return data in sequence format ascending or descending
orderbyquery = "SELECT * FROM userss ORDER BY salary DESC"
mycursor.execute(orderbyquery)
print(mycursor.fetchall())
connection.commit()



###-----STRING FUNCTION-----
##CONCAT()----is used to combine two or more strings into one.
concatquery = "SELECT CONCAT(name, ' ', email) FROM userss"
mycursor.execute(concatquery)
print(mycursor.fetchall())
connection.commit()


##LOWER()---- is used to convert a string to lowercase.
lowerquery = "SELECT LOWER(name) FROM userss"
mycursor.execute(lowerquery)
print(mycursor.fetchall())
connection.commit()


##UPPER()---- is used to convert a string to uppercase.
upperquery = "SELECT UPPER(name) FROM userss"
mycursor.execute(upperquery)
print(mycursor.fetchall())
connection.commit()


##TRIM()----is used to remove unwanted characters from the beginning and end of a string.
trimquery = "SELECT TRIM(name) FROM userss"
mycursor.execute(trimquery)
print(mycursor.fetchall())
connection.commit()


##LENGTH()----is used to return the number of characters (or bytes, depending on the database system) in a string.
lengthquery = "SELECT LENGTH(name) FROM userss"
mycursor.execute(lengthquery)
print(mycursor.fetchall())
connection.commit()


##SUBSTRING----is used to extract a portion of a string from a given position for a specified length.
substringquery = "SELECT SUBSTRING(name, 1, 5) FROM userss"
mycursor.execute(substringquery)
print(mycursor.fetchall())
connection.commit()



###Update table
query = "UPDATE userss SET salary = 50000 WHERE name = 'Jane Smith'"
mycursor.execute(query)
print(mycursor.rowcount, "record(s) affected")
connection.commit()

#Update name
upadtequery = "UPDATE userss SET name = %s WHERE id = 2"
new_name = "jane Smith"
mycursor.execute(upadtequery, (new_name,))
print(mycursor.rowcount, "record(s) affected")
connection.commit()



###Delete----DELETE remove the specific row based on the given condition 
query = "DELETE FROM userss WHERE name = %s"
data = ("Jane Smith",)
mycursor.execute(query, data)
print(mycursor.rowcount, "record(s) affected")
connection.commit()



###Truncate----TRUNCATE removes all the record from the table at once.
query = "TRUNCATE TABLE userss"
mycursor.execute(query)
print(mycursor.rowcount, "record(s) affected")
connection.commit()



###ALTER----is used to modify the structure of an existing table. It allows you to add, delete, or modify columns, 
###               as well as make other structural changes like renaming a table or altering constraints.
query = "ALTER TABLE userss ADD COLUMN phone_number VARCHAR(15)"
mycursor.execute(query)
print(mycursor.rowcount, "record(s) affected")
connection.commit()



###DROP TABLE----DROP command removes the table or databases and as well as the structure.
query = "DROP TABLE userss"
mycursor.execute(query)
print(mycursor.rowcount, "record(s) affected")
connection.commit()

##-----[END]-----
