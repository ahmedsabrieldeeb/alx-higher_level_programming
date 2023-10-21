-- This script lists all cities in Califoria state
-- The cities must be sorted ascendingly based on cities.id
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;

