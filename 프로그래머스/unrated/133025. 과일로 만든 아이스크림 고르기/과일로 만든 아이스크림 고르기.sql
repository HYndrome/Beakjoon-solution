-- 코드를 입력하세요
SELECT
    FH.FLAVOR
FROM
    FIRST_HALF FH
LEFT JOIN ICECREAM_INFO INFO
    ON FH.FLAVOR = INFO.FLAVOR
WHERE
    FH.TOTAL_ORDER > 3000
    AND INFO.INGREDIENT_TYPE = 'fruit_based'
ORDER BY
    FH.TOTAL_ORDER DESC;
