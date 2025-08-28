# Airbnb Database Seed Script

## Objective
This script inserts **sample data** into the Airbnb database schema.  
It is designed to reflect **real-world usage** with multiple users, properties, bookings, payments, reviews, and messages.

---

## Files
- `seed.sql` → SQL `INSERT` statements for sample data.
- `README.md` → This documentation.

---

## Entities Covered
1. **User** → 5 users (guests, hosts, admin).
2. **Property** → 2 properties listed by different hosts.
3. **Booking** → 2 bookings (confirmed + pending).
4. **Payment** → Payments linked to bookings.
5. **Review** → Reviews from users about properties.
6. **Message** → Direct messages between users.

---

## Usage
Run the script after creating the schema:

```bash
mysql -u <username> -p < database-script-0x01/schema.sql
mysql -u <username> -p < database-script-0x02/seed.sql
