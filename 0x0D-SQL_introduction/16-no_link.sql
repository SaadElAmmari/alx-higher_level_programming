-- list all record of the table second_table having a name value in my MySQL server.
-- record are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
