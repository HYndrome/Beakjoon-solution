-- 코드를 입력하세요

SELECT
    member.MEMBER_NAME,
    rev.REVIEW_TEXT,
    DATE_FORMAT(rev.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM
    REST_REVIEW AS rev
LEFT JOIN MEMBER_PROFILE AS member
    ON rev.MEMBER_ID = member.MEMBER_ID
WHERE
    rev.MEMBER_ID IN (
    SELECT
        MEMBER_ID
    FROM
        REST_REVIEW
    GROUP BY
        MEMBER_ID
    HAVING
        COUNT(*) = (
            SELECT
                COUNT(*)
            FROM
                REST_REVIEW
            GROUP BY
                MEMBER_ID
            ORDER BY
                COUNT(*) DESC
            LIMIT 1
            )
        )
ORDER BY
    REVIEW_DATE,
    REVIEW_TEXT