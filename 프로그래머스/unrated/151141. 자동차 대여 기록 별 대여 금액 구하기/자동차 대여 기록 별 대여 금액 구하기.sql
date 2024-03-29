-- 코드를 입력하세요
SELECT
    HISTORY_ID,
    ROUND(ORIGINAL_FEE * (100 - IFNULL(DISCOUNT_RATE, 0)) / 100, 0) AS 'FEE'
FROM
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN discount_plans
RIGHT JOIN (
    SELECT
        HISTORY_ID,
        CAR_TYPE,
        START_DATE,
        END_DATE,
        DATEDIFF(END_DATE, START_DATE) + 1 AS 'RENTAL_TERM',
        (DATEDIFF(END_DATE, START_DATE) + 1) * DAILY_FEE AS 'ORIGINAL_FEE',
        CASE
            WHEN (DATEDIFF(END_DATE, START_DATE) + 1) < 7 THEN NULL
            WHEN (DATEDIFF(END_DATE, START_DATE) + 1) < 30 THEN '7일 이상'
            WHEN (DATEDIFF(END_DATE, START_DATE) + 1) < 90 THEN '30일 이상'
            ELSE '90일 이상'
        END AS 'DURATION_TYPE'
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY histories
    LEFT JOIN CAR_RENTAL_COMPANY_CAR plans
        ON histories.CAR_ID = plans.CAR_ID
    WHERE
        CAR_TYPE = '트럭'    
    ) truck_fees
    ON discount_plans.CAR_TYPE = truck_fees.CAR_TYPE AND discount_plans.DURATION_TYPE = truck_fees.DURATION_TYPE
HAVING
    FEE IS NOT NULL
ORDER BY
    FEE DESC,
    HISTORY_ID DESC