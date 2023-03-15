-- Lists all records with score >= 10 in the table second_table of the database in your MySQL server.
-- The records are ordered by score (descending)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
