-- 코드를 입력하세요
WITH RECURSIVE CTE AS (
    SELECT 0 AS hours
    UNION ALL
    SELECT hours + 1 FROM CTE WHERE hours < 23
    )
    
SELECT
    CTE.hours as 'HOUR',
    CASE
        WHEN COUNT1 IS NULL THEN '0'
        ELSE COUNT1
    END AS 'COUNT'
FROM
    CTE
LEFT JOIN (
    SELECT
        HOUR(DATETIME) AS 'HOUR',
        COUNT(ANIMAL_ID) AS 'COUNT1'
    FROM
        ANIMAL_OUTS
    GROUP BY
        DATE_FORMAT(DATETIME, '%H')
    ORDER BY
        HOUR(DATETIME)
    ) AS INS
    ON CTE.hours = INS.HOUR
ORDER BY
    HOUR