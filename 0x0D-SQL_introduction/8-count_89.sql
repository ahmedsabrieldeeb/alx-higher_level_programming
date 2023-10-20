-- This scripts countes number of records matching a specific criteria
-- Using COUNT function, we can aggregate on rows of tables
SELECT COUNT(id)
AS number_of_records_where_id_equals_11
FROM first_table
WHERE id = 89;

