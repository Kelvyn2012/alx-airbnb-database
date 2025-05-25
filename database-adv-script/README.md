# alx-airbnb-database

# SQL Joins – Airbnb Database Project

This section of the project demonstrates the use of SQL joins to retrieve related data across multiple tables in the simulated Airbnb database. The goal is to master INNER JOIN, LEFT JOIN, and FULL OUTER JOIN operations by writing real-world queries.

## ✅ Task Objectives

- Retrieve bookings with corresponding users using INNER JOIN.
- Retrieve properties and their reviews using LEFT JOIN, including properties that have no reviews.
- Retrieve all users and all bookings using FULL OUTER JOIN (or a UNION workaround for MySQL).

## 🔍 Queries Overview

### 1. INNER JOIN – Bookings and Users

```sql
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
```

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

# Subqueries – Airbnb Database Project

This section of the project focuses on mastering subqueries in SQL. You will learn to use both correlated and non-correlated subqueries to retrieve data based on calculations and nested logic.

## ✅ Task Objectives

- Use a non-correlated subquery to find high-rated properties.
- Use a correlated subquery to find users with more than 3 bookings.

## 🔍 Queries Overview

### 1. Non-Correlated Subquery – High-Rated Properties

```sql
SELECT id, name
FROM properties
WHERE id IN (
    SELECT property_id
    FROM reviews
    GROUP BY property_id
    HAVING AVG(rating) > 4.0
)
ORDER BY id;

```

SELECT id, first_name, last_name
FROM users u
WHERE (
SELECT COUNT(\*)
FROM bookings b
WHERE b.user_id = u.id
) > 3
ORDER BY id;
