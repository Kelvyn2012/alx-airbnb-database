-- 1. INNER JOIN: Get all bookings and the users who made them
SELECT
    b.id AS booking_id,
    b.start_date,
    b.end_date,
    u.id AS user_id,
    u.first_name,
    u.last_name
FROM
    bookings b
INNER JOIN
    users u ON b.user_id = u.id
ORDER BY
    b.start_date;

-- 2. LEFT JOIN: Get all properties and their reviews (including properties with no reviews)
SELECT
    p.id AS property_id,
    p.name AS property_name,
    r.id AS review_id,
    r.rating,
    r.comment
FROM
    properties p
LEFT JOIN
    reviews r ON p.id = r.property_id
ORDER BY
    p.id;

-- 3. FULL OUTER JOIN: Get all users and bookings, even if no match exists

-- PostgreSQL version
SELECT
    u.id AS user_id,
    u.first_name,
    u.last_name,
    b.id AS booking_id,
    b.start_date,
    b.end_date
FROM
    users u
FULL OUTER JOIN
    bookings b ON u.id = b.user_id
ORDER BY
    u.id NULLS LAST, b.id;

-- MySQL version using UNION
SELECT
    u.id AS user_id,
    u.first_name,
    u.last_name,
    b.id AS booking_id,
    b.start_date,
    b.end_date
FROM
    users u
LEFT JOIN
    bookings b ON u.id = b.user_id

UNION

SELECT
    u.id AS user_id,
    u.first_name,
    u.last_name,
    b.id AS booking_id,
    b.start_date,
    b.end_date
FROM
    users u
RIGHT JOIN
    bookings b ON u.id = b.user_id
ORDER BY
    user_id;
