DROP TABLE countries;

-- Create Table
CREATE TABLE countries (
country VARCHAR(100),
population REAL,
fertility REAL,
continent VARCHAR(25)
)
;


-- Fill the table
COPY countries
FROM '/Users/stefanroth/spiced/cohorts/logistic-lemongrass-encounter-notes/week_06/large_countries_2015.csv'
DELIMITER ','
CSV HEADER;


-- Alter your table
ALTER TABLE countries
ALTER COLUMN population TYPE INTEGER;


-- SELECT
-- Select all values
SELECT *
FROM countries;



-- Select only the columns country and population
SELECT country, population
FROM countries;
-- SELECT column(s)
-- FROM table;



-- DISTINCT
-- Select the distinct continents
SELECT DISTINCT continent
FROM countries;


-- Apply a condition using WHERE
-- What if I was only interested in Asian countries, but I wanted to have all information on them
SELECT *
FROM countries
WHERE continent = 'Asia';



-- Select only the columns country and population and order by population size
SELECT country, population
FROM countries
WHERE continent = 'Asia'
ORDER BY population DESC;
-- ORDER BY is in ascending order by default
-- ORDER BY column(s) [DESC]


-- LIMIT our query
-- Select the three countries with the highest fertility rate
SELECT country, fertility
FROM countries
ORDER BY fertility DESC
LIMIT 3;



-- What if we only wanted Asia to appear


-- With LIKE we can also look for patterns in string
-- Select all countries which start with "I"
SELECT country
FROM countries
WHERE country LIKE 'I%';


-- Multiple
-- Select all countries which start with "I" and have more than 200,000,000 inhabitants
SELECT country
FROM countries
WHERE country LIKE 'I%' OR population > 300000000;



-- GROUPING, AGGREGATE RESULTS
-- Show the average population by continent
SELECT continent, AVG(population)
FROM countries
GROUP BY continent;



-- Applying a condition on a grouped by table, you will have to use HAVING
-- Show the average population by continent if it exceeds 300,000,000
SELECT continent, AVG(population)
FROM countries
GROUP BY continent
HAVING AVG(population) > 300000000
;



-- Subqueries: Using an intermediate query as input table for the final query
SELECT *
FROM (
	SELECT continent, AVG(population) as average_population
	FROM countries
	GROUP BY continent) AS subquery
WHERE average_population > 300000000;


WITH subquery AS (
	SELECT continent, AVG(population) as average_population
	FROM countries
	GROUP BY continent)

SELECT *
FROM subquery
WHERE average_population > 300000000;



-- CASE basically is an if statement in SQL
-- Update South America and North America to The Americas
SELECT country,
		CASE
			WHEN continent = 'North America' THEN 'The Americas'
			WHEN continent = 'South America' THEN 'The Americas'
			ELSE continent
		END as updated_continent
FROM countries;


-- We want to make this change permanent
UPDATE countries
SET continent = CASE
					WHEN continent IN ('North America', 'South America') THEN 'The Americas'
--					WHEN continent = 'South America' THEN 'The Americas'
					ELSE continent
			  	END;


SELECT *
FROM countries;




-- Add a new column
ALTER TABLE countries
ADD COLUMN new_column INTEGER DEFAULT 1;

SELECT *
FROM countries;



-- Delete rows from a table
DELETE FROM countries
WHERE continent IS NULL;



-- Delete all entries from a table
TRUNCATE TABLE countries;

SELECT *
FROM countries;



-- Delete whole database table
DROP TABLE countries;



-- Delete whole database
DROP DATABASE countries;
