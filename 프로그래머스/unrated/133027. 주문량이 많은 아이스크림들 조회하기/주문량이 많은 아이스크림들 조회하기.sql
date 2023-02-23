-- 코드를 입력하세요
SELECT
    FLAVOR
FROM
    (
    SELECT
        FLAVOR,
        TOTAL_ORDER
    FROM
        FIRST_HALF
    UNION
    SELECT
        FLAVOR,
        TOTAL_ORDER
    FROM    
        JULY
    ) AS T
GROUP BY
    FLAVOR
ORDER BY
    SUM(TOTAL_ORDER) DESC
LIMIT 3