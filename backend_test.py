#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Ayurvedic Plants App
Tests all backend endpoints with proper authentication flow
"""

import requests
import json
import base64
import os
from typing import Dict, Any

# Backend URL from environment
BACKEND_URL = "https://ayurved-detect.preview.emergentagent.com/api"

class AyurvedicPlantsAPITester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.auth_token = None
        self.test_user = {
            "username": "testplant",
            "password": "plant123"
        }
        self.results = {
            "auth": {},
            "plants": {},
            "identification": {},
            "scan_history": {}
        }
        
    def log_result(self, category: str, test_name: str, success: bool, details: str = ""):
        """Log test results"""
        if category not in self.results:
            self.results[category] = {}
        self.results[category][test_name] = {
            "success": success,
            "details": details
        }
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {category.upper()}: {test_name}")
        if details:
            print(f"    Details: {details}")
    
    def create_test_image_base64(self) -> str:
        """Create a small test image in base64 format"""
        # Simple 1x1 pixel PNG in base64
        return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
    
    def test_root_endpoint(self):
        """Test the root API endpoint"""
        try:
            response = requests.get(f"{self.base_url}")
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "Ayurvedic Plants API" in data["message"]:
                    self.log_result("general", "root_endpoint", True, f"API version: {data.get('version', 'N/A')}")
                    return True
                else:
                    self.log_result("general", "root_endpoint", False, f"Unexpected response: {data}")
                    return False
            else:
                self.log_result("general", "root_endpoint", False, f"Status: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("general", "root_endpoint", False, f"Error: {str(e)}")
            return False
    
    def test_user_registration(self):
        """Test user registration endpoint"""
        try:
            response = requests.post(
                f"{self.base_url}/auth/register",
                json=self.test_user
            )
            
            if response.status_code == 200:
                data = response.json()
                if "access_token" in data and "username" in data:
                    self.auth_token = data["access_token"]
                    self.log_result("auth", "registration", True, f"User: {data['username']}, Token received")
                    return True
                else:
                    self.log_result("auth", "registration", False, f"Missing token or username in response: {data}")
                    return False
            elif response.status_code == 400:
                # User might already exist, try to continue with login
                self.log_result("auth", "registration", True, "User already exists (expected)")
                return True
            else:
                self.log_result("auth", "registration", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("auth", "registration", False, f"Error: {str(e)}")
            return False
    
    def test_user_login(self):
        """Test user login endpoint"""
        try:
            response = requests.post(
                f"{self.base_url}/auth/login",
                json=self.test_user
            )
            
            if response.status_code == 200:
                data = response.json()
                if "access_token" in data and "username" in data:
                    self.auth_token = data["access_token"]
                    self.log_result("auth", "login", True, f"User: {data['username']}, Token: {self.auth_token[:20]}...")
                    return True
                else:
                    self.log_result("auth", "login", False, f"Missing token or username: {data}")
                    return False
            else:
                self.log_result("auth", "login", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("auth", "login", False, f"Error: {str(e)}")
            return False
    
    def test_protected_endpoint_me(self):
        """Test protected /auth/me endpoint"""
        if not self.auth_token:
            self.log_result("auth", "protected_me", False, "No auth token available")
            return False
        
        try:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            response = requests.get(f"{self.base_url}/auth/me", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if "username" in data and "user_id" in data:
                    self.log_result("auth", "protected_me", True, f"User: {data['username']}, ID: {data['user_id']}")
                    return True
                else:
                    self.log_result("auth", "protected_me", False, f"Missing user data: {data}")
                    return False
            else:
                self.log_result("auth", "protected_me", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("auth", "protected_me", False, f"Error: {str(e)}")
            return False
    
    def test_get_all_plants(self):
        """Test GET /plants endpoint"""
        try:
            response = requests.get(f"{self.base_url}/plants")
            
            if response.status_code == 200:
                data = response.json()
                if "plants" in data and "total" in data:
                    plants_count = len(data["plants"])
                    total_count = data["total"]
                    self.log_result("plants", "get_all", True, f"Retrieved {plants_count} plants, Total: {total_count}")
                    
                    # Store first plant ID for detail test
                    if plants_count > 0:
                        self.first_plant_id = data["plants"][0]["_id"]
                        self.first_plant_name = data["plants"][0]["name"]
                    
                    return True
                else:
                    self.log_result("plants", "get_all", False, f"Missing plants or total in response: {data}")
                    return False
            else:
                self.log_result("plants", "get_all", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("plants", "get_all", False, f"Error: {str(e)}")
            return False
    
    def test_search_plants(self):
        """Test plant search functionality"""
        try:
            # Search for Tulsi (should be in seeded data)
            response = requests.get(f"{self.base_url}/plants?search=Tulsi")
            
            if response.status_code == 200:
                data = response.json()
                if "plants" in data:
                    plants_count = len(data["plants"])
                    if plants_count > 0:
                        found_tulsi = any(plant["name"].lower() == "tulsi" for plant in data["plants"])
                        if found_tulsi:
                            self.log_result("plants", "search", True, f"Found {plants_count} plants matching 'Tulsi'")
                        else:
                            self.log_result("plants", "search", True, f"Search returned {plants_count} results (no exact Tulsi match)")
                    else:
                        self.log_result("plants", "search", False, "Search returned no results")
                    return True
                else:
                    self.log_result("plants", "search", False, f"Missing plants in response: {data}")
                    return False
            else:
                self.log_result("plants", "search", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("plants", "search", False, f"Error: {str(e)}")
            return False
    
    def test_get_plant_details(self):
        """Test GET /plants/{id} endpoint"""
        if not hasattr(self, 'first_plant_id'):
            self.log_result("plants", "get_details", False, "No plant ID available from previous test")
            return False
        
        try:
            response = requests.get(f"{self.base_url}/plants/{self.first_plant_id}")
            
            if response.status_code == 200:
                data = response.json()
                required_fields = ["_id", "name", "scientific_name", "family", "description", 
                                 "characteristics", "medicinal_properties", "uses", "parts_used"]
                
                missing_fields = [field for field in required_fields if field not in data]
                if not missing_fields:
                    self.log_result("plants", "get_details", True, f"Plant: {data['name']} ({data['scientific_name']})")
                    return True
                else:
                    self.log_result("plants", "get_details", False, f"Missing fields: {missing_fields}")
                    return False
            else:
                self.log_result("plants", "get_details", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("plants", "get_details", False, f"Error: {str(e)}")
            return False
    
    def test_plant_identification(self):
        """Test POST /plants/identify endpoint"""
        if not self.auth_token:
            self.log_result("identification", "identify_plant", False, "No auth token available")
            return False
        
        try:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            test_image = self.create_test_image_base64()
            
            payload = {"image_base64": test_image}
            response = requests.post(
                f"{self.base_url}/plants/identify",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                required_fields = ["plant_name", "confidence", "characteristics", 
                                 "medicinal_properties", "matches_database", "scan_id"]
                
                missing_fields = [field for field in required_fields if field not in data]
                if not missing_fields:
                    self.log_result("identification", "identify_plant", True, 
                                  f"Identified: {data['plant_name']}, Confidence: {data['confidence']}, Scan ID: {data['scan_id']}")
                    self.scan_id = data["scan_id"]
                    return True
                else:
                    self.log_result("identification", "identify_plant", False, f"Missing fields: {missing_fields}")
                    return False
            else:
                self.log_result("identification", "identify_plant", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("identification", "identify_plant", False, f"Error: {str(e)}")
            return False
    
    def test_scan_history(self):
        """Test GET /scans/history endpoint"""
        if not self.auth_token:
            self.log_result("scan_history", "get_history", False, "No auth token available")
            return False
        
        try:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            response = requests.get(f"{self.base_url}/scans/history", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if "scans" in data:
                    scans_count = len(data["scans"])
                    if scans_count > 0:
                        # Check if our recent scan is in the history
                        recent_scan = data["scans"][0]
                        required_fields = ["_id", "user_id", "identified_plant_name", "confidence"]
                        missing_fields = [field for field in required_fields if field not in recent_scan]
                        
                        if not missing_fields:
                            self.log_result("scan_history", "get_history", True, 
                                          f"Found {scans_count} scans, Latest: {recent_scan['identified_plant_name']}")
                        else:
                            self.log_result("scan_history", "get_history", False, f"Missing fields in scan: {missing_fields}")
                    else:
                        self.log_result("scan_history", "get_history", True, "No scan history found (expected for new user)")
                    return True
                else:
                    self.log_result("scan_history", "get_history", False, f"Missing scans in response: {data}")
                    return False
            else:
                self.log_result("scan_history", "get_history", False, f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_result("scan_history", "get_history", False, f"Error: {str(e)}")
            return False
    
    def test_invalid_auth(self):
        """Test endpoints with invalid authentication"""
        try:
            # Test with invalid token
            headers = {"Authorization": "Bearer invalid_token_12345"}
            response = requests.get(f"{self.base_url}/auth/me", headers=headers)
            
            if response.status_code == 401:
                self.log_result("auth", "invalid_token", True, "Correctly rejected invalid token")
                return True
            else:
                self.log_result("auth", "invalid_token", False, f"Expected 401, got {response.status_code}")
                return False
        except Exception as e:
            self.log_result("auth", "invalid_token", False, f"Error: {str(e)}")
            return False
    
    def test_invalid_plant_id(self):
        """Test plant details with invalid ID"""
        try:
            response = requests.get(f"{self.base_url}/plants/invalid_id_123")
            
            if response.status_code == 400:
                self.log_result("plants", "invalid_id", True, "Correctly rejected invalid plant ID")
                return True
            else:
                self.log_result("plants", "invalid_id", False, f"Expected 400, got {response.status_code}")
                return False
        except Exception as e:
            self.log_result("plants", "invalid_id", False, f"Error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all backend API tests"""
        print("=" * 60)
        print("AYURVEDIC PLANTS API - BACKEND TESTING")
        print("=" * 60)
        print(f"Testing backend at: {self.base_url}")
        print()
        
        # Test sequence
        tests = [
            ("General API", self.test_root_endpoint),
            ("Authentication - Registration", self.test_user_registration),
            ("Authentication - Login", self.test_user_login),
            ("Authentication - Protected Endpoint", self.test_protected_endpoint_me),
            ("Plants - Get All", self.test_get_all_plants),
            ("Plants - Search", self.test_search_plants),
            ("Plants - Get Details", self.test_get_plant_details),
            ("Plant Identification", self.test_plant_identification),
            ("Scan History", self.test_scan_history),
            ("Error Handling - Invalid Auth", self.test_invalid_auth),
            ("Error Handling - Invalid Plant ID", self.test_invalid_plant_id)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            print(f"\n--- {test_name} ---")
            if test_func():
                passed += 1
        
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        # Detailed results
        print("\nDETAILED RESULTS:")
        for category, tests in self.results.items():
            print(f"\n{category.upper()}:")
            for test_name, result in tests.items():
                status = "✅" if result["success"] else "❌"
                print(f"  {status} {test_name}: {result['details']}")
        
        return passed == total

if __name__ == "__main__":
    tester = AyurvedicPlantsAPITester()
    success = tester.run_all_tests()
    exit(0 if success else 1)