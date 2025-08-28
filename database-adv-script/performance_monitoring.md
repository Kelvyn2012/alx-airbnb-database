# Performance Monitoring and Refinement Report

## Monitored Query

```sql
SELECT
    b.id,
    b.start_date,
    u.first_name,
    p.name AS property_name
FROM bookings b
JOIN users u ON b.user_id = u.id
JOIN properties p ON b.property_id = p.id
WHERE b.start_date >= '2024-01-01'
  AND u.country = 'Nigeria'
ORDER BY b.start_date DESC;
```
