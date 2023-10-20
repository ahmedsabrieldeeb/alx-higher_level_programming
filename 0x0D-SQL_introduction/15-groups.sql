-- This script lists the number of records with the same score
-- Using SELECT, GROUP BY
SELECT score, COUNT(*) AS number -- SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;

