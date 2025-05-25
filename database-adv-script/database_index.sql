-- Index on users.id (often joined with bookings.user_id)
CREATE INDEX idx_users_id ON users(id);

-- Index on bookings.user_id (used in joins and filters)
CREATE INDEX idx_bookings_user_id ON bookings(user_id);

-- Index on bookings.property_id (used in joins with properties)
CREATE INDEX idx_bookings_property_id ON bookings(property_id);

-- Index on bookings.start_date (useful for filtering by date range)
CREATE INDEX idx_bookings_start_date ON bookings(start_date);

-- Index on properties.id (used in joins with bookings and reviews)
CREATE INDEX idx_properties_id ON properties(id);
