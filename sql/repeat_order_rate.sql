SELECT
    COUNT(DISTINCT user_id) AS repeat_users
FROM
(
    SELECT user_id
    FROM orders
    GROUP BY user_id
    HAVING COUNT(*) >= 2
) t;