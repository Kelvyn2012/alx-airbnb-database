#!/usr/bin/env python3
"""
Full endpoint testing with authentication for Airbnb Clone API
"""
import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:8001"
headers = {"Content-Type": "application/json"}

def print_section(title: str):
    """Print a section header"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def test_result(name, success, details=""):
    """Print test result"""
    status = "✓ PASS" if success else "✗ FAIL"
    color = "\033[92m" if success else "\033[91m"
    reset = "\033[0m"
    print(f"{color}{status}{reset} | {name}")
    if details:
        print(f"       {details}")
    return success

def main():
    passed = 0
    failed = 0

    print_section("AIRBNB CLONE API - FULL AUTHENTICATED TEST")
    print(f"Base URL: {BASE_URL}")
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # =============================================================================
    # 1. USER REGISTRATION AND LOGIN
    # =============================================================================
    print_section("1. USER AUTHENTICATION")

    # Register a new user
    timestamp = datetime.now().timestamp()
    user_data = {
        "email": f"testuser_{timestamp}@example.com",
        "password": "TestPassword123!",
        "password_confirm": "TestPassword123!",
        "first_name": "Test",
        "last_name": "User",
        "phone_number": "+1234567890",
        "role": "guest"
    }

    response = requests.post(f"{BASE_URL}/api/users/register/", json=user_data, headers=headers)
    if test_result("User Registration", response.status_code == 201, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1
        print(f"       Response: {response.text[:200]}")

    # Login
    login_data = {"email": user_data["email"], "password": user_data["password"]}
    response = requests.post(f"{BASE_URL}/api/users/login/", json=login_data, headers=headers)

    auth_token = None
    refresh_token = None
    if response.status_code == 200:
        data = response.json()
        auth_token = data.get("access")
        refresh_token = data.get("refresh")
        if test_result("User Login", auth_token is not None, f"Token obtained: {auth_token[:20]}..."):
            passed += 1
        else:
            failed += 1
    else:
        test_result("User Login", False, f"Status: {response.status_code}")
        failed += 1

    if not auth_token:
        print("\n\033[91mAuthentication failed. Stopping tests.\033[0m\n")
        return 1

    # Set auth headers
    auth_headers = headers.copy()
    auth_headers["Authorization"] = f"Bearer {auth_token}"

    # Test token refresh
    if refresh_token:
        response = requests.post(f"{BASE_URL}/api/users/token/refresh/",
                               json={"refresh": refresh_token}, headers=headers)
        if test_result("Token Refresh", response.status_code == 200, f"Status: {response.status_code}"):
            passed += 1
        else:
            failed += 1

    # Get user profile
    response = requests.get(f"{BASE_URL}/api/users/profile/", headers=auth_headers)
    if test_result("Get User Profile", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # =============================================================================
    # 2. PROPERTY OPERATIONS
    # =============================================================================
    print_section("2. PROPERTY OPERATIONS")

    # List all properties
    response = requests.get(f"{BASE_URL}/api/properties/", headers=headers)
    if test_result("List All Properties (Public)", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # Create a property (change role to host first by registering as host)
    host_data = {
        "email": f"testhost_{timestamp}@example.com",
        "password": "TestPassword123!",
        "password_confirm": "TestPassword123!",
        "first_name": "Host",
        "last_name": "User",
        "phone_number": "+1234567891",
        "role": "host"
    }

    response = requests.post(f"{BASE_URL}/api/users/register/", json=host_data, headers=headers)
    if response.status_code == 201:
        # Login as host
        host_login = {"email": host_data["email"], "password": host_data["password"]}
        response = requests.post(f"{BASE_URL}/api/users/login/", json=host_login, headers=headers)
        if response.status_code == 200:
            host_token = response.json().get("access")
            host_headers = headers.copy()
            host_headers["Authorization"] = f"Bearer {host_token}"

            # Create property
            property_data = {
                "title": "Beautiful Beach House",
                "description": "A stunning beachfront property with amazing views",
                "price_per_night": 150.00,
                "location": "Miami Beach, FL",
                "bedrooms": 3,
                "bathrooms": 2,
                "max_guests": 6,
            }

            response = requests.post(f"{BASE_URL}/api/properties/create/",
                                   json=property_data, headers=host_headers)
            property_id = None
            if response.status_code == 201:
                property_id = response.json().get("property_id")
                if test_result("Create Property", True, f"Property ID: {property_id}"):
                    passed += 1
                else:
                    failed += 1
            else:
                test_result("Create Property", False, f"Status: {response.status_code}, Response: {response.text[:200]}")
                failed += 1

            # Get my properties
            response = requests.get(f"{BASE_URL}/api/properties/my-properties/", headers=host_headers)
            if test_result("Get My Properties", response.status_code == 200, f"Status: {response.status_code}"):
                passed += 1
            else:
                failed += 1

            # Get property detail
            if property_id:
                response = requests.get(f"{BASE_URL}/api/properties/{property_id}/", headers=headers)
                if test_result("Get Property Detail", response.status_code == 200, f"Status: {response.status_code}"):
                    passed += 1
                else:
                    failed += 1

    # =============================================================================
    # 3. BOOKING OPERATIONS
    # =============================================================================
    print_section("3. BOOKING OPERATIONS")

    # List user's bookings
    response = requests.get(f"{BASE_URL}/api/bookings/", headers=auth_headers)
    if test_result("List My Bookings", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # Create a booking if we have a property
    if property_id:
        booking_data = {
            "property_id": property_id,
            "check_in": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
            "check_out": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
            "number_of_guests": 4
        }

        response = requests.post(f"{BASE_URL}/api/bookings/create/",
                               json=booking_data, headers=auth_headers)
        booking_id = None
        if response.status_code == 201:
            booking_id = response.json().get("booking_id")
            if test_result("Create Booking", True, f"Booking ID: {booking_id}"):
                passed += 1
            else:
                failed += 1
        else:
            test_result("Create Booking", False, f"Status: {response.status_code}, Response: {response.text[:200]}")
            failed += 1

        # Get booking detail
        if booking_id:
            response = requests.get(f"{BASE_URL}/api/bookings/{booking_id}/", headers=auth_headers)
            if test_result("Get Booking Detail", response.status_code == 200, f"Status: {response.status_code}"):
                passed += 1
            else:
                failed += 1

    # Get host bookings
    if host_token:
        response = requests.get(f"{BASE_URL}/api/bookings/host/", headers=host_headers)
        if test_result("Get Host Bookings", response.status_code == 200, f"Status: {response.status_code}"):
            passed += 1
        else:
            failed += 1

    # =============================================================================
    # 4. REVIEW OPERATIONS
    # =============================================================================
    print_section("4. REVIEW OPERATIONS")

    # List reviews for a property
    if property_id:
        response = requests.get(f"{BASE_URL}/api/reviews/property/{property_id}/", headers=headers)
        if test_result("List Property Reviews", response.status_code == 200, f"Status: {response.status_code}"):
            passed += 1
        else:
            failed += 1

        # Create a review
        review_data = {
            "property_id": property_id,
            "rating": 5,
            "comment": "Amazing place! Highly recommended!"
        }

        response = requests.post(f"{BASE_URL}/api/reviews/create/",
                               json=review_data, headers=auth_headers)
        review_id = None
        if response.status_code == 201:
            review_id = response.json().get("review_id")
            if test_result("Create Review", True, f"Review ID: {review_id}"):
                passed += 1
            else:
                failed += 1
        else:
            test_result("Create Review", False, f"Status: {response.status_code}, Response: {response.text[:200]}")
            failed += 1

        # Get review detail
        if review_id:
            response = requests.get(f"{BASE_URL}/api/reviews/{review_id}/", headers=auth_headers)
            if test_result("Get Review Detail", response.status_code == 200, f"Status: {response.status_code}"):
                passed += 1
            else:
                failed += 1

    # =============================================================================
    # 5. PAYMENT OPERATIONS
    # =============================================================================
    print_section("5. PAYMENT OPERATIONS")

    # List user's payments
    response = requests.get(f"{BASE_URL}/api/payments/", headers=auth_headers)
    if test_result("List My Payments", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # =============================================================================
    # 6. MESSAGE OPERATIONS
    # =============================================================================
    print_section("6. MESSAGE OPERATIONS")

    # List user's messages
    response = requests.get(f"{BASE_URL}/api/messages/", headers=auth_headers)
    if test_result("List My Messages", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # =============================================================================
    # 7. API DOCUMENTATION
    # =============================================================================
    print_section("7. API DOCUMENTATION")

    # Swagger UI
    response = requests.get(f"{BASE_URL}/swagger/", headers=headers)
    if test_result("Swagger Documentation", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # ReDoc
    response = requests.get(f"{BASE_URL}/redoc/", headers=headers)
    if test_result("ReDoc Documentation", response.status_code == 200, f"Status: {response.status_code}"):
        passed += 1
    else:
        failed += 1

    # =============================================================================
    # SUMMARY
    # =============================================================================
    print_section("TEST SUMMARY")

    total = passed + failed
    success_rate = (passed / total * 100) if total > 0 else 0

    print(f"Total Tests:    {total}")
    print(f"✓ Passed:       \033[92m{passed}\033[0m ({success_rate:.1f}%)")
    print(f"✗ Failed:       \033[91m{failed}\033[0m ({100-success_rate:.1f}%)")
    print(f"\n{'='*70}\n")

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    try:
        exit(main())
    except Exception as e:
        print(f"\n\033[91mError during testing: {str(e)}\033[0m\n")
        exit(1)
