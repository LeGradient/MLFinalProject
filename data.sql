CREATE TABLE ml2016
SELECT
    '2016' AS 'year',
    hc_key AS 'region',
    ownership,
    COUNT( CASE WHEN (division = 'I' OR division = 'DISTINCTION' OR division = 'II' OR division = 'MERIT' OR division = 'III' OR division = 'CREDIT' OR division = 'IV' OR division = 'PASS') THEN 1 END ) / COUNT(*) AS 'passrate'
FROM `2016` JOIN MASTER ON `2016`.necta = MASTER.necta
GROUP BY `2016`.necta;