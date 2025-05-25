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
    users u ON b.user_id = u.id;

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
    reviews r ON p.id = r.property_id;

-- 3. FULL OUTER JOIN: Get all users and all bookings, even if no match exists
-- Note: FULL OUTER JOIN is not supported in MySQL. If you're using PostgreSQL, this works.
-- If you're using MySQL, simulate it using UNION.

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
    bookings b ON u.id = b.user_id;

-- MySQL alternative using UNION
-- SELECT from users LEFT JOIN bookings
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

-- SELECT from bookings RIGHT JOIN users
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
    bookings b ON u.id = b.user_id;
