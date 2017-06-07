-- CREATE TABLE ml2012
-- SELECT
--     '2012' AS 'year',
--     hc_key AS 'region',
--     ownership,
--     gender,
--     COUNT( CASE WHEN (division = 'I' OR division = 'DISTINCTION' OR division = 'II' OR division = 'MERIT' OR division = 'III' OR division = 'CREDIT' OR division = 'IV' OR division = 'PASS') THEN 1 END ) / COUNT(*) AS 'passrate',
--     COUNT( CASE WHEN (division = 'I' OR division = 'DISTINCTION') THEN 1 END ) / COUNT(*) AS 'div1rate',
--     COUNT( CASE WHEN (division = 'II' OR division = 'MERIT') THEN 1 END ) / COUNT(*) AS 'div2rate',
--     COUNT( CASE WHEN (division = 'III' OR division = 'CREDIT') THEN 1 END ) / COUNT(*) AS 'div3rate',
--     COUNT( CASE WHEN (division = 'IV' OR division = 'PASS') THEN 1 END ) / COUNT(*) AS 'div4rate'
-- FROM `2012` JOIN MASTER ON `2012`.necta = MASTER.necta
-- WHERE gender = 'F'
-- GROUP BY `2012`.necta

-- UNION ALL

-- SELECT
--     '2012' AS 'year',
--     hc_key AS 'region',
--     ownership,
--     gender,
--     COUNT( CASE WHEN (division = 'I' OR division = 'DISTINCTION' OR division = 'II' OR division = 'MERIT' OR division = 'III' OR division = 'CREDIT' OR division = 'IV' OR division = 'PASS') THEN 1 END ) / COUNT(*) AS 'passrate',
--     COUNT( CASE WHEN (division = 'I' OR division = 'DISTINCTION') THEN 1 END ) / COUNT(*) AS 'div1rate',
--     COUNT( CASE WHEN (division = 'II' OR division = 'MERIT') THEN 1 END ) / COUNT(*) AS 'div2rate',
--     COUNT( CASE WHEN (division = 'III' OR division = 'CREDIT') THEN 1 END ) / COUNT(*) AS 'div3rate',
--     COUNT( CASE WHEN (division = 'IV' OR division = 'PASS') THEN 1 END ) / COUNT(*) AS 'div4rate'
-- FROM `2012` JOIN MASTER ON `2012`.necta = MASTER.necta
-- WHERE gender = 'M'
-- GROUP BY `2012`.necta;

SELECT * INTO OUTFILE '/tmp/mysql/ml2012.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM ml2012;