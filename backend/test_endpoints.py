#!/usr/bin/env python3
"""
Comprehensive endpoint testing script for Airbnb Clone API
Tests all endpoints to verify they're working correctly
"""
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, Any

BASE_URL = "http://localhost:8001"
headers = {"Content-Type": "application/json"}
auth_token = None

# Test results tracker
test_results = {
    "passed": [],
    "failed": [],
    "total": 0
}

def print_section(title: str):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def print_test_result(endpoint: str, method: str, status_code: int, expected: int, response_data: Any = None):
    """Print test result"""
    test_results["total"] += 1
    passed = status_code == expected

    status = "✓ PASS" if passed else "✗ FAIL"
    color = "\033[92m" if passed else "\033[91m"
    reset = "\033[0m"

    print(f"{color}{status}{reset} | {method:6} | {endpoint:50} | Status: {status_code} (expected {expected})")

    if passed:
        test_results["passed"].append(f"{method} {endpoint}")
    else:
        test_results["failed"].append(f"{method} {endpoint} - got {status_code}, expected {expected}")
        if response_data:
            print(f"       Response: {json.dumps(response_data, indent=2)[:200]}")

def test_endpoint(method: str, endpoint: str, expected_status: int, data: Dict = None, auth: bool = False):
    """Test an API endpoint"""
    url = f"{BASE_URL}{endpoint}"
    request_headers = headers.copy()

    if auth and auth_token:
        request_headers["Authorization"] = f"Bearer {auth_token}"

    try:
        if method == "GET":
            response = requests.get(url, headers=request_headers)
        elif method == "POST":
            response = requests.post(url, headers=request_headers, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=request_headers, json=data)
        elif method == "PATCH":
            response = requests.patch(url, headers=request_headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=request_headers)
        else:
            print(f"Unknown method: {method}")
            return None

        try:
            response_data = response.json() if response.text else None
        except:
            response_data = response.text

        print_test_result(endpoint, method, response.status_code, expected_status, response_data)
        return response
    except requests.exceptions.ConnectionError:
        print(f"\033[91m✗ FAIL\033[0m | {method:6} | {endpoint:50} | Connection Error - Server not running?")
        test_results["failed"].append(f"{method} {endpoint} - Connection Error")
        return None
    except Exception as e:
        print(f"\033[91m✗ FAIL\033[0m | {method:6} | {endpoint:50} | Error: {str(e)}")
        test_results["failed"].append(f"{method} {endpoint} - {str(e)}")
        return None

def main():
    global auth_token

    print_section("AIRBNB CLONE API - ENDPOINT TESTING")
    print(f"Base URL: {BASE_URL}")
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # =============================================================================
    # 1. USER AUTHENTICATION ENDPOINTS
    # =============================================================================
    print_section("1. USER AUTHENTICATION ENDPOINTS")

    # Test user registration
    test_data = {
        "email": f"testuser_{datetime.now().timestamp()}@example.com",
        "password": "TestPassword123!",
        "password_confirm": "TestPassword123!",
        "first_name": "Test",
        "last_name": "User",
        "phone_number": "+1234567890",
        "role": "guest"
    }
    response = test_endpoint("POST", "/api/users/register/", 201, test_data)

    # Test user login
    login_data = {
        "email": test_data["email"],
        "password": test_data["password"]
    }
    response = test_endpoint("POST", "/api/users/login/", 200, login_data)
    if response and response.status_code == 200:
        try:
            auth_token = response.json().get("access")
            print(f"\n✓ Authentication token obtained\n")
        except:
            print(f"\n✗ Failed to extract auth token\n")

    # Test token refresh
    if response and response.status_code == 200:
        try:
            refresh_token = response.json().get("refresh")
            test_endpoint("POST", "/api/users/token/refresh/", 200, {"refresh": refresh_token})
        except:
            test_endpoint("POST", "/api/users/token/refresh/", 400, {"refresh": "invalid_token"})

    # Test user profile (requires auth)
    test_endpoint("GET", "/api/users/profile/", 401 if not auth_token else 200, auth=True)

    # Test OAuth endpoints (these will return 200 with redirect HTML)
    test_endpoint("GET", "/api/users/auth/google/", 200)
    test_endpoint("GET", "/api/users/auth/facebook/", 200)

    # =============================================================================
    # 2. PROPERTY ENDPOINTS
    # =============================================================================
    print_section("2. PROPERTY ENDPOINTS")

    # List properties (public)
    test_endpoint("GET", "/api/properties/", 200)

    # Create property (requires auth)
    property_data = {
        "name": "Beautiful Beach House",
        "description": "A stunning beachfront property with amazing views",
        "pricepernight": 150.00,
        "location": "Miami Beach, FL",
        "bedrooms": 3,
        "bathrooms": 2,
        "max_guests": 6,
        "amenities": "wifi,pool,parking"
    }
    response = test_endpoint("POST", "/api/properties/create/", 401 if not auth_token else 201, property_data, auth=True)

    property_id = None
    if response and response.status_code == 201:
        try:
            property_id = response.json().get("property_id")
        except:
            pass

    # Get my properties (requires auth)
    test_endpoint("GET", "/api/properties/my-properties/", 401 if not auth_token else 200, auth=True)

    # Get property detail (use a dummy UUID)
    test_property_id = property_id if property_id else "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/properties/{test_property_id}/", 200 if property_id else 404)

    # Upload property image (requires auth)
    if property_id:
        test_endpoint("POST", f"/api/properties/{property_id}/images/", 401 if not auth_token else 400, auth=True)

    # =============================================================================
    # 3. BOOKING ENDPOINTS
    # =============================================================================
    print_section("3. BOOKING ENDPOINTS")

    # List bookings (requires auth)
    test_endpoint("GET", "/api/bookings/", 401 if not auth_token else 200, auth=True)

    # Create booking (requires auth)
    if property_id:
        booking_data = {
            "property_id": property_id,
            "check_in": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
            "check_out": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
            "number_of_guests": 4
        }
        response = test_endpoint("POST", "/api/bookings/create/", 401 if not auth_token else 201, booking_data, auth=True)

    # Get host bookings (requires auth)
    test_endpoint("GET", "/api/bookings/host/", 401 if not auth_token else 200, auth=True)

    # Get booking detail (use a dummy UUID)
    test_booking_id = "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/bookings/{test_booking_id}/", 401 if not auth_token else 404, auth=True)

    # =============================================================================
    # 4. REVIEW ENDPOINTS
    # =============================================================================
    print_section("4. REVIEW ENDPOINTS")

    # List reviews for a property (returns empty list for non-existent property)
    test_property_id = property_id if property_id else "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/reviews/property/{test_property_id}/", 200)

    # Create review (requires auth)
    if property_id:
        review_data = {
            "property_id": property_id,
            "rating": 5,
            "comment": "Amazing place! Highly recommended!"
        }
        test_endpoint("POST", "/api/reviews/create/", 401 if not auth_token else 201, review_data, auth=True)

    # Get review detail (use a dummy UUID - requires auth)
    test_review_id = "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/reviews/{test_review_id}/", 401 if not auth_token else 404, auth=True)

    # =============================================================================
    # 5. PAYMENT ENDPOINTS
    # =============================================================================
    print_section("5. PAYMENT ENDPOINTS")

    # List payments (requires auth)
    test_endpoint("GET", "/api/payments/", 401 if not auth_token else 200, auth=True)

    # Create payment (requires auth)
    payment_data = {
        "booking_id": "00000000-0000-0000-0000-000000000000",
        "amount": 450.00,
        "payment_method": "stripe"
    }
    test_endpoint("POST", "/api/payments/create/", 401 if not auth_token else 400, payment_data, auth=True)

    # Get payment detail (use a dummy UUID)
    test_payment_id = "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/payments/{test_payment_id}/", 401 if not auth_token else 404, auth=True)

    # =============================================================================
    # 6. MESSAGE ENDPOINTS
    # =============================================================================
    print_section("6. MESSAGE ENDPOINTS")

    # List messages (requires auth)
    test_endpoint("GET", "/api/messages/", 401 if not auth_token else 200, auth=True)

    # Create message (requires auth)
    message_data = {
        "receiver_id": "00000000-0000-0000-0000-000000000000",
        "message_body": "Hello, is this property still available?"
    }
    test_endpoint("POST", "/api/messages/create/", 401 if not auth_token else 400, message_data, auth=True)

    # Get conversation (requires auth)
    test_user_id = "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/messages/conversation/{test_user_id}/", 401 if not auth_token else 200, auth=True)

    # Get message detail (use a dummy UUID)
    test_message_id = "00000000-0000-0000-0000-000000000000"
    test_endpoint("GET", f"/api/messages/{test_message_id}/", 401 if not auth_token else 404, auth=True)

    # =============================================================================
    # 7. API DOCUMENTATION ENDPOINTS
    # =============================================================================
    print_section("7. API DOCUMENTATION ENDPOINTS")

    # Swagger UI
    test_endpoint("GET", "/swagger/", 200)

    # ReDoc
    test_endpoint("GET", "/redoc/", 200)

    # Admin panel (returns login page - 200)
    test_endpoint("GET", "/admin/", 200)

    # =============================================================================
    # SUMMARY
    # =============================================================================
    print_section("TEST SUMMARY")

    total = test_results["total"]
    passed = len(test_results["passed"])
    failed = len(test_results["failed"])
    success_rate = (passed / total * 100) if total > 0 else 0

    print(f"Total Tests:    {total}")
    print(f"✓ Passed:       {passed} ({success_rate:.1f}%)")
    print(f"✗ Failed:       {failed} ({100-success_rate:.1f}%)")

    if failed > 0:
        print(f"\n\nFailed Tests:")
        print(f"{'-'*60}")
        for failure in test_results["failed"]:
            print(f"  ✗ {failure}")

    print(f"\n{'='*60}\n")

    # Return exit code based on failures
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    exit(main())
