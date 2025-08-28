# Index Performance Report

## Indexed Columns

- users.id
- bookings.user_id
- bookings.property_id
- bookings.start_date
- properties.id

## Before Indexing

The following query took ~120ms:

```sql
EXPLAIN ANALYZE
SELECT b.id, u.first_name, p.name
FROM bookings b
JOIN users u ON b.user_id = u.id
JOIN properties p ON b.property_id = p.id
WHERE b.start_date >= '2024-01-01'
ORDER BY b.start_date DESC;
```
