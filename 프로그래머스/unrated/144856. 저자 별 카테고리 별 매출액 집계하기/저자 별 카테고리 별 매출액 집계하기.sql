-- 코드를 입력하세요
SELECT
    info.AUTHOR_ID,
    author.AUTHOR_NAME,
    info.CATEGORY,
    SUM(info.PRICE * sales.SALES) AS TOTAL_SALES
FROM
    BOOK_SALES sales
LEFT JOIN BOOK info
    ON sales.BOOK_ID = info.BOOK_ID
LEFT JOIN AUTHOR author
    ON info.AUTHOR_ID = author.AUTHOR_ID
WHERE
    DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY
    author.AUTHOR_NAME, info.CATEGORY
ORDER BY
    AUTHOR_ID,
    CATEGORY DESC
