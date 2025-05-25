-- Step 1: Create partitioned table
CREATE TABLE bookings_partitioned (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    property_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY RANGE (start_date);

-- Step 2: Create partitions (example: quarterly partitions)
CREATE TABLE bookings_2024_q1 PARTITION OF bookings_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE bookings_2024_q2 PARTITION OF bookings_partitioned
    FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

CREATE TABLE bookings_2024_q3 PARTITION OF bookings_partitioned
    FOR VALUES FROM ('2024-07-01') TO ('2024-10-01');

CREATE TABLE bookings_2024_q4 PARTITION OF bookings_partitioned
    FOR VALUES FROM ('2024-10-01') TO ('2025-01-01');

-- Step 3: Query to test performance
EXPLAIN ANALYZE
SELECT * FROM bookings_partitioned
WHERE start_date BETWEEN '2024-01-01' AND '2024-03-31';
