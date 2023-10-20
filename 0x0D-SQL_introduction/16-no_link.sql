-- This script lists all records only with names existed
-- SELECT, ORDER, IS statements
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

