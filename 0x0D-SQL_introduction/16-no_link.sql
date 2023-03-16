-- Lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Records are in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
