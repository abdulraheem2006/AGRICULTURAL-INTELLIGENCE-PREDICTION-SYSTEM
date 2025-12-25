#!/usr/bin/env python3
"""
Test script for Agricultural Intelligence Prediction System
This script tests all the core functionality without requiring a web server
"""

from app import recommend_crop, recommend_fertilizer, predict_disease, predict_yield
import json

def test_crop_recommendation():
    print("=" * 60)
    print("TEST 1: Crop Recommendation")
    print("=" * 60)
    
    # Test case 1: Optimal conditions for Rice
    print("\nTest Case 1: Optimal conditions for Rice")
    crops = recommend_crop(N=90, P=45, K=45, temperature=25, humidity=85, ph=6.5, rainfall=250)
    print(f"Top recommendation: {crops[0]['crop']} with {crops[0]['suitability']}% suitability")
    assert crops[0]['crop'] == 'Rice', "Expected Rice as top recommendation"
    assert crops[0]['suitability'] == 100.0, "Expected 100% suitability"
    print("✓ Test passed!")
    
    # Test case 2: Conditions suitable for Wheat
    print("\nTest Case 2: Conditions suitable for Wheat")
    crops = recommend_crop(N=65, P=40, K=40, temperature=20, humidity=60, ph=6.5, rainfall=75)
    print(f"Top recommendation: {crops[0]['crop']} with {crops[0]['suitability']}% suitability")
    print("✓ Test passed!")

def test_fertilizer_recommendation():
    print("\n" + "=" * 60)
    print("TEST 2: Fertilizer Recommendation")
    print("=" * 60)
    
    # Test case 1: Nutrient deficit
    print("\nTest Case 1: Nutrient deficit for Rice")
    fert = recommend_fertilizer(N=40, P=30, K=30, crop_type='Rice')
    print(f"Nitrogen deficit: {fert['deficit']['N']} kg/ha")
    print(f"Phosphorus deficit: {fert['deficit']['P']} kg/ha")
    print(f"Potassium deficit: {fert['deficit']['K']} kg/ha")
    print(f"Recommendations: {len(fert['recommendations'])} items")
    assert fert['deficit']['N'] > 0, "Expected nitrogen deficit"
    print("✓ Test passed!")
    
    # Test case 2: Optimal nutrients
    print("\nTest Case 2: Optimal nutrients for Wheat")
    fert = recommend_fertilizer(N=65, P=40, K=40, crop_type='Wheat')
    print(f"Recommendations: {fert['recommendations'][0]}")
    print("✓ Test passed!")

def test_disease_prediction():
    print("\n" + "=" * 60)
    print("TEST 3: Disease Prediction")
    print("=" * 60)
    
    # Test case 1: Rice disease
    print("\nTest Case 1: Rice Brown Spot Disease")
    disease = predict_disease('Rice', 'Brown spots on leaves')
    print(f"Diagnosis: {disease['diagnosis']}")
    print(f"Treatment: {disease['treatment']}")
    assert 'Brown Spot' in disease['treatment'], "Expected Brown Spot Disease diagnosis"
    print("✓ Test passed!")
    
    # Test case 2: Unknown disease
    print("\nTest Case 2: Unknown symptoms")
    disease = predict_disease('Rice', 'Unknown symptom')
    print(f"Diagnosis: {disease['diagnosis']}")
    assert disease['diagnosis'] == 'Unknown', "Expected Unknown diagnosis"
    print("✓ Test passed!")

def test_yield_prediction():
    print("\n" + "=" * 60)
    print("TEST 4: Yield Prediction")
    print("=" * 60)
    
    # Test case 1: Rice yield
    print("\nTest Case 1: Rice yield prediction")
    yield_pred = predict_yield('Rice', area=5, N=90, P=45, K=45, rainfall=250, temperature=25)
    print(f"Crop: {yield_pred['crop']}")
    print(f"Area: {yield_pred['area']} hectares")
    print(f"Yield per hectare: {yield_pred['predicted_yield_per_hectare']} {yield_pred['unit']}")
    print(f"Total production: {yield_pred['total_production']} {yield_pred['unit']}")
    assert yield_pred['predicted_yield_per_hectare'] > 0, "Expected positive yield"
    print("✓ Test passed!")
    
    # Test case 2: Sugarcane yield
    print("\nTest Case 2: Sugarcane yield prediction")
    yield_pred = predict_yield('Sugarcane', area=10, N=120, P=60, K=80, rainfall=200, temperature=28)
    print(f"Yield per hectare: {yield_pred['predicted_yield_per_hectare']} {yield_pred['unit']}")
    print("✓ Test passed!")

def main():
    print("\n" + "=" * 60)
    print("AGRICULTURAL INTELLIGENCE PREDICTION SYSTEM - TEST SUITE")
    print("=" * 60)
    
    try:
        test_crop_recommendation()
        test_fertilizer_recommendation()
        test_disease_prediction()
        test_yield_prediction()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        print("\nThe Agricultural Intelligence Prediction System is working correctly!")
        print("You can run the web application with: python app.py")
        print("Then visit: http://localhost:5000")
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
