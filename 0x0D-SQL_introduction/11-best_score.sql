-- This script lists rows after a threshold basedo on field score
-- Using ORDER statement and WHERE to put a condition
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

