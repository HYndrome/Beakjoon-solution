-- 코드를 입력하세요
SELECT
    APNT_NO,
    PT_NAME,
    app.PT_NO,
    app.MCDP_CD,
    DR_NAME,
    APNT_YMD
FROM
    APPOINTMENT app
LEFT JOIN
    PATIENT pat
    ON app.PT_NO = pat.PT_NO
LEFT JOIN
    DOCTOR doc
    ON app.MDDR_ID = doc.DR_ID
WHERE
    DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
    AND APNT_CNCL_YN = 'N'
    AND app.MCDP_CD = 'CS'
ORDER BY
    APNT_YMD;