# Partitioning Performance Report

## Partitioning Strategy

We partitioned the `bookings` table by RANGE on the `start_date` column to improve performance when querying by date.

- 4 partitions created: Q1, Q2, Q3, and Q4 for the year 2024.

## Test Query

```sql
SELECT * FROM bookings_partitioned
WHERE start_date BETWEEN '2024-01-01' AND '2024-03-31';
```
