WITH temp AS (
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
)
SELECT id
FROM temp
WHERE temperature > prev_temp
AND DATEDIFF(DAY, prev_date, recordDate) = 1;