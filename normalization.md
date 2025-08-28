# Airbnb Database Normalization

## Objective
Apply normalization principles to ensure the Airbnb database schema is in **Third Normal Form (3NF)**.

---

## Step 1: First Normal Form (1NF)
- Ensure all attributes are **atomic** (no repeating groups, no multi-valued attributes).
- ✅ Our schema already satisfies 1NF:
  - Each field holds a single value (e.g., `first_name`, `last_name`).
  - No arrays or repeating columns.

---

## Step 2: Second Normal Form (2NF)
- Ensure the table is in **1NF** and all **non-key attributes** depend on the **whole primary key**.
- ✅ Since every table uses a **single-column primary key (UUIDs)**:
  - No partial dependency issues.
  - For example, in **Booking**, `start_date`, `end_date`, and `status` all depend on the `booking_id` (not part of a composite key).

---

## Step 3: Third Normal Form (3NF)
- Ensure the table is in **2NF** and **non-key attributes** depend only on the primary key, not on other non-key attributes (**no transitive dependencies**).

### Review of Entities

#### User
- Attributes: personal info (`first_name`, `last_name`, `email`), authentication (`password_hash`), role (`guest`, `host`, `admin`).
- ✅ All fields depend directly on `user_id`.
- No transitive dependencies.

#### Property
- Attributes: descriptive info (`name`, `description`, `location`), pricing (`pricepernight`).
- ✅ All fields depend directly on `property_id`.
- `host_id` is a foreign key → valid dependency.
- No redundancies.

#### Booking
- Attributes: dates, `total_price`, `status`.
- Potential issue: `total_price` could be derived from `pricepernight × number_of_nights`.
  - To maintain 3NF, derived/calculated fields should ideally not be stored.
  - **Option 1 (normalized)**: Remove `total_price` and compute it dynamically.
  - **Option 2 (denormalized for performance)**: Keep `total_price` but note that it violates strict 3NF.
- ⚠️ For 3NF, we would remove `total_price`.

#### Payment
- Attributes: amount, method, date.
- ✅ All fields depend directly on `payment_id`.
- No issues.

#### Review
- Attributes: `rating`, `comment`.
- ✅ All fields depend on `review_id`.
- No issues.

#### Message
- Attributes: `message_body`, `sent_at`.
- ✅ All fields depend on `message_id`.
- No issues.

---

## Normalization Summary
- **1NF**: Achieved (no repeating groups, atomic attributes).
- **2NF**: Achieved (single-column primary keys).
- **3NF**: Achieved, **except for `Booking.total_price`** which introduces a derived value.
  - ✅ Recommended fix: Remove `total_price` from the schema and compute it from `Property.pricepernight × (end_date - start_date)`.

---

## Final Note
The schema is **fully normalized to 3NF** if `Booking.total_price` is removed.  
If performance considerations require keeping `total_price`, document it as a **controlled denormalization**.

