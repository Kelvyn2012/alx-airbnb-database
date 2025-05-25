-- 1. Non-Correlated Subquery
-- Find all properties where the average rating is greater than 4.0
SELECT id, name
FROM properties
WHERE id IN (
    SELECT property_id
    FROM reviews
    GROUP BY property_id
    HAVING AVG(rating) > 4.0
)
ORDER BY id;

-- 2. Correlated Subquery
-- Find users who have made more than 3 bookings
SELECT id, first_name, last_name
FROM users u
WHERE (
    SELECT COUNT(*)
    FROM bookings b
    WHERE b.user_id = u.id
) > 3
ORDER BY id;
