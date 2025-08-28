-- Airbnb Sample Data (Seed Script)
-- =====================
-- Insert Users
-- =====================
INSERT INTO
    User (
        user_id,
        first_name,
        last_name,
        email,
        password_hash,
        phone_number,
        role
    )
VALUES
    (
        '11111111-1111-1111-1111-111111111111',
        'Alice',
        'Johnson',
        'alice@example.com',
        'hashed_pw1',
        '1234567890',
        'guest'
    ),
    (
        '22222222-2222-2222-2222-222222222222',
        'Bob',
        'Smith',
        'bob@example.com',
        'hashed_pw2',
        '2345678901',
        'host'
    ),
    (
        '33333333-3333-3333-3333-333333333333',
        'Charlie',
        'Brown',
        'charlie@example.com',
        'hashed_pw3',
        '3456789012',
        'host'
    ),
    (
        '44444444-4444-4444-4444-444444444444',
        'Diana',
        'Lopez',
        'diana@example.com',
        'hashed_pw4',
        '4567890123',
        'guest'
    ),
    (
        '55555555-5555-5555-5555-555555555555',
        'Ethan',
        'Williams',
        'ethan@example.com',
        'hashed_pw5',
        '5678901234',
        'admin'
    );

-- =====================
-- Insert Properties
-- =====================
INSERT INTO
    Property (
        property_id,
        host_id,
        name,
        description,
        location,
        pricepernight
    )
VALUES
    (
        'aaaa1111-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        '22222222-2222-2222-2222-222222222222',
        'Cozy Apartment',
        'A small but cozy apartment near downtown.',
        'New York, USA',
        120.00
    ),
    (
        'bbbb2222-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        '33333333-3333-3333-3333-333333333333',
        'Beach House',
        'Spacious beach house with ocean view.',
        'Miami, USA',
        300.00
    );

-- =====================
-- Insert Bookings
-- =====================
INSERT INTO
    Booking (
        booking_id,
        property_id,
        user_id,
        start_date,
        end_date,
        total_price,
        status
    )
VALUES
    (
        'book1111-1111-1111-1111-111111111111',
        'aaaa1111-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        '11111111-1111-1111-1111-111111111111',
        '2025-09-01',
        '2025-09-05',
        480.00,
        'confirmed'
    ),
    (
        'book2222-2222-2222-2222-222222222222',
        'bbbb2222-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        '44444444-4444-4444-4444-444444444444',
        '2025-10-10',
        '2025-10-15',
        1500.00,
        'pending'
    );

-- =====================
-- Insert Payments
-- =====================
INSERT INTO
    Payment (payment_id, booking_id, amount, payment_method)
VALUES
    (
        'pay1111-1111-1111-1111-111111111111',
        'book1111-1111-1111-1111-111111111111',
        480.00,
        'credit_card'
    ),
    (
        'pay2222-2222-2222-2222-222222222222',
        'book2222-2222-2222-2222-222222222222',
        1500.00,
        'paypal'
    );

-- =====================
-- Insert Reviews
-- =====================
INSERT INTO
    Review (review_id, property_id, user_id, rating, comment)
VALUES
    (
        'rev1111-1111-1111-1111-111111111111',
        'aaaa1111-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
        '11111111-1111-1111-1111-111111111111',
        5,
        'Great stay! Very clean and comfortable.'
    ),
    (
        'rev2222-2222-2222-2222-222222222222',
        'bbbb2222-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
        '44444444-4444-4444-4444-444444444444',
        4,
        'Amazing view but a bit pricey.'
    );

-- =====================
-- Insert Messages
-- =====================
INSERT INTO
    Message (message_id, sender_id, recipient_id, message_body)
VALUES
    (
        'msg1111-1111-1111-1111-111111111111',
        '11111111-1111-1111-1111-111111111111',
        '22222222-2222-2222-2222-222222222222',
        'Hi Bob, is your apartment available next weekend?'
    ),
    (
        'msg2222-2222-2222-2222-222222222222',
        '22222222-2222-2222-2222-222222222222',
        '11111111-1111-1111-1111-111111111111',
        'Hi Alice, yes it is available from Friday to Sunday.'
    );