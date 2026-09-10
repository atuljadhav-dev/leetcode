-- /* Write your PL/SQL query statement below */
-- select 
--     s.student_id,
--     s.subject,
--     s.score first_score,
--     ss.score latest_score
-- from scores s
-- join scores ss
-- on s.student_id=ss.student_id
-- and s.subject=ss.subject
-- and s.exam_date<ss.exam_date
-- and s.score<ss.score
-- where (s.exam_date,ss.exam_date) in (select
--                                             min(exam_date),
--                                             max(exam_date)
--                                     from scores sss
--                                     where ss.student_id=sss.student_id
--                                     and ss.subject=sss.subject)
-- order by student_id, subject;
SELECT *
FROM(
    SELECT 
        DISTINCT student_id, 
        subject,
        FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) AS first_score,
        FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_score
    FROM Scores
)
WHERE latest_score > first_score
ORDER BY student_id, subject ASC