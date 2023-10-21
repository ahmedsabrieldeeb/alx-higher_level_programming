-- This script lists all cities in the database passed as an argument
-- JOIN statement is used to achieve that
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id;

