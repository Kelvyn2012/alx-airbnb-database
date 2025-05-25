-- 1. Total number of bookings made by each user
SELECT 
    u.id AS user_id,
    u.first_name,
    u.last_name,
    COUNT(b.id) AS total_bookings
FROM 
    users u
JOIN 
    bookings b ON u.id = b.user_id
GROUP BY 
    u.id, u.first_name, u.last_name
ORDER BY 
    total_bookings DESC;

-- 2. Rank properties based on total bookings using RANK()
SELECT 
    p.id AS property_id,
    p.name AS property_name,
    COUNT(b.id) AS total_bookings,
    RANK() OVER (ORDER BY COUNT(b.id) DESC) AS booking_rank
FROM 
    properties p
LEFT JOIN 
    bookings b ON p.id = b.property_id
GROUP BY 
    p.id, p.name
ORDER BY 
    booking_rank;

-- 3. Rank properties based on total bookings using ROW_NUMBER()
SELECT 
    p.id AS property_id,
    p.name AS property_name,
    COUNT(b.id) AS total_bookings,
    ROW_NUMBER() OVER (ORDER BY COUNT(b.id) DESC) AS row_num
FROM 
    properties p
LEFT JOIN 
    bookings b ON p.id = b.property_id
GROUP BY 
    p.id, p.name
ORDER BY 
    row_num;
