# Airbnb Database Schema (SQL)

## Objective
This script defines the **Airbnb database schema** using SQL `CREATE TABLE` statements.  
It includes all **entities, attributes, primary keys, foreign keys, and constraints** as described in the specification.

---

## Files
- `schema.sql` → Contains the SQL schema (create tables, constraints, indexes).
- `README.md` → This documentation.

---

## Entities
1. **User** → Stores user information (guest, host, admin).
2. **Property** → Represents properties listed by hosts.
3. **Booking** → Tracks reservations made by users.
4. **Payment** → Stores payment details linked to bookings.
5. **Review** → Contains reviews users leave on properties.
6. **Message** → Stores user-to-user communication.

---

## Constraints
- **Primary Keys**: All tables use `UUID` as primary keys.
- **Foreign Keys**:
  - `Property.host_id` → `User.user_id`
  - `Booking.property_id` → `Property.property_id`
  - `Booking.user_id` → `User.user_id`
  - `Payment.booking_id` → `Booking.booking_id`
  - `Review.property_id` → `Property.property_id`
  - `Review.user_id` → `User.user_id`
  - `Message.sender_id` and `recipient_id` → `User.user_id`
- **Unique**: `User.email` must be unique.
- **Checks**:
  - `Review.rating` between 1 and 5.
  - `Booking.status` restricted to `pending`, `confirmed`, `canceled`.
  - `Payment.payment_method` restricted to `credit_card`, `paypal`, `stripe`.

---

## Indexing
Indexes have been added for:
- `User.email` (to speed up lookups by email).
- `Property.host_id` (to quickly find properties by host).
- `Booking.property_id` and `Booking.user_id` (for queries by property or user).
- `Payment.booking_id` (to retrieve payments by booking).

---

## Usage
Run the schema script in your SQL environment:

```bash
mysql -u <username> -p < schema.sql
