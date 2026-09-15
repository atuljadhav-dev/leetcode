/* Write your PL/SQL query statement below */
WITH FirstPositive AS (
    SELECT 
        patient_id, 
        MIN(test_date) AS first_pos_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
FirstNegativeAfterPositive AS (
    SELECT 
        t.patient_id, 
        MIN(t.test_date) AS first_neg_date
    FROM covid_tests t
    JOIN FirstPositive fp 
        ON t.patient_id = fp.patient_id 
        AND t.test_date > fp.first_pos_date
    WHERE t.result = 'Negative'
    GROUP BY t.patient_id
)
SELECT 
    p.patient_id,
    p.patient_name,
    p.age,
    fn.first_neg_date-fp.first_pos_date AS recovery_time
FROM FirstPositive fp
JOIN FirstNegativeAfterPositive fn 
ON fp.patient_id = fn.patient_id
JOIN patients p 
ON p.patient_id = fp.patient_id
ORDER BY recovery_time, p.patient_name;
