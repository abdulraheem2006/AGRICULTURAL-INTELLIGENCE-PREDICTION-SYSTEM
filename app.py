from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load datasets
try:
    crop_data = pd.read_csv('data/crop_data.csv')
except:
    crop_data = None

# Crop recommendation based on NPK values and environmental conditions
def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    """
    Recommend crop based on soil and environmental parameters
    N: Nitrogen content
    P: Phosphorus content
    K: Potassium content
    temperature: Temperature in Celsius
    humidity: Relative humidity in %
    ph: pH value of soil
    rainfall: Rainfall in mm
    """
    crop_requirements = {
        'Rice': {'N': (80, 120), 'P': (40, 60), 'K': (40, 60), 'temp': (20, 30), 'humidity': (80, 90), 'ph': (5.5, 7.0), 'rainfall': (200, 300)},
        'Wheat': {'N': (50, 80), 'P': (30, 50), 'K': (30, 50), 'temp': (15, 25), 'humidity': (50, 70), 'ph': (6.0, 7.5), 'rainfall': (50, 100)},
        'Maize': {'N': (60, 100), 'P': (40, 60), 'K': (40, 60), 'temp': (18, 27), 'humidity': (60, 80), 'ph': (5.5, 7.0), 'rainfall': (80, 150)},
        'Cotton': {'N': (60, 100), 'P': (30, 50), 'K': (30, 50), 'temp': (21, 30), 'humidity': (50, 80), 'ph': (6.0, 8.0), 'rainfall': (60, 120)},
        'Sugarcane': {'N': (80, 150), 'P': (40, 80), 'K': (60, 100), 'temp': (20, 30), 'humidity': (70, 90), 'ph': (6.0, 7.5), 'rainfall': (150, 250)},
        'Potato': {'N': (50, 80), 'P': (50, 80), 'K': (50, 80), 'temp': (15, 25), 'humidity': (70, 90), 'ph': (5.5, 6.5), 'rainfall': (50, 100)},
        'Tomato': {'N': (40, 70), 'P': (40, 70), 'K': (40, 70), 'temp': (20, 30), 'humidity': (60, 80), 'ph': (6.0, 7.0), 'rainfall': (60, 100)},
        'Banana': {'N': (100, 200), 'P': (50, 100), 'K': (150, 300), 'temp': (25, 35), 'humidity': (75, 95), 'ph': (6.0, 7.5), 'rainfall': (200, 400)},
        'Coffee': {'N': (60, 100), 'P': (30, 50), 'K': (60, 100), 'temp': (15, 25), 'humidity': (60, 80), 'ph': (6.0, 6.5), 'rainfall': (150, 250)},
        'Tea': {'N': (80, 120), 'P': (40, 60), 'K': (40, 60), 'temp': (20, 30), 'humidity': (70, 90), 'ph': (4.5, 5.5), 'rainfall': (150, 300)},
    }
    
    recommendations = []
    for crop, requirements in crop_requirements.items():
        score = 0
        max_score = 7
        
        if requirements['N'][0] <= N <= requirements['N'][1]:
            score += 1
        if requirements['P'][0] <= P <= requirements['P'][1]:
            score += 1
        if requirements['K'][0] <= K <= requirements['K'][1]:
            score += 1
        if requirements['temp'][0] <= temperature <= requirements['temp'][1]:
            score += 1
        if requirements['humidity'][0] <= humidity <= requirements['humidity'][1]:
            score += 1
        if requirements['ph'][0] <= ph <= requirements['ph'][1]:
            score += 1
        if requirements['rainfall'][0] <= rainfall <= requirements['rainfall'][1]:
            score += 1
        
        suitability = (score / max_score) * 100
        if suitability >= 50:
            recommendations.append({'crop': crop, 'suitability': round(suitability, 2)})
    
    recommendations.sort(key=lambda x: x['suitability'], reverse=True)
    return recommendations[:5] if recommendations else [{'crop': 'No suitable crop found', 'suitability': 0}]

# Fertilizer recommendation
def recommend_fertilizer(N, P, K, crop_type):
    """Recommend fertilizer based on NPK values and crop type"""
    fertilizer_recommendations = {
        'Rice': {'N': 100, 'P': 50, 'K': 50},
        'Wheat': {'N': 60, 'P': 40, 'K': 40},
        'Maize': {'N': 80, 'P': 50, 'K': 50},
        'Cotton': {'N': 80, 'P': 40, 'K': 40},
        'Sugarcane': {'N': 120, 'P': 60, 'K': 80},
        'Potato': {'N': 65, 'P': 65, 'K': 65},
        'Tomato': {'N': 55, 'P': 55, 'K': 55},
        'Banana': {'N': 150, 'P': 75, 'K': 225},
        'Coffee': {'N': 80, 'P': 40, 'K': 80},
        'Tea': {'N': 100, 'P': 50, 'K': 50},
    }
    
    if crop_type not in fertilizer_recommendations:
        return {'message': 'Crop type not found in database'}
    
    required = fertilizer_recommendations[crop_type]
    deficit_N = max(0, required['N'] - N)
    deficit_P = max(0, required['P'] - P)
    deficit_K = max(0, required['K'] - K)
    
    recommendations = []
    if deficit_N > 0:
        recommendations.append(f"Add {deficit_N} kg/ha of Nitrogen (Urea: {deficit_N * 2.17:.1f} kg/ha)")
    if deficit_P > 0:
        recommendations.append(f"Add {deficit_P} kg/ha of Phosphorus (DAP: {deficit_P * 2.17:.1f} kg/ha)")
    if deficit_K > 0:
        recommendations.append(f"Add {deficit_K} kg/ha of Potassium (MOP: {deficit_K * 1.67:.1f} kg/ha)")
    
    if not recommendations:
        recommendations.append("Your soil has optimal nutrient levels for this crop!")
    
    return {
        'current': {'N': N, 'P': P, 'K': K},
        'required': required,
        'deficit': {'N': deficit_N, 'P': deficit_P, 'K': deficit_K},
        'recommendations': recommendations
    }

# Crop disease prediction (simplified version)
def predict_disease(crop, symptoms):
    """Predict crop disease based on symptoms"""
    disease_database = {
        'Rice': {
            'Brown spots on leaves': 'Brown Spot Disease - Apply fungicide, improve drainage',
            'Yellow leaves': 'Nitrogen deficiency - Apply nitrogen fertilizer',
            'White powdery coating': 'Blast Disease - Apply Tricyclazole fungicide',
        },
        'Wheat': {
            'Orange pustules': 'Rust Disease - Apply fungicide, use resistant varieties',
            'Yellow leaves': 'Nitrogen deficiency - Apply nitrogen fertilizer',
            'Black spots on grains': 'Smut Disease - Use treated seeds',
        },
        'Tomato': {
            'Brown spots on leaves': 'Early Blight - Apply fungicide, remove infected leaves',
            'Curled leaves': 'Virus infection - Remove infected plants, control aphids',
            'Yellow leaves': 'Nutrient deficiency - Apply balanced fertilizer',
        },
        'Potato': {
            'Black spots on leaves': 'Late Blight - Apply fungicide, improve air circulation',
            'Curled leaves': 'Leaf Roll Virus - Use certified seeds, control aphids',
            'Yellow leaves': 'Nutrient deficiency - Apply balanced fertilizer',
        }
    }
    
    if crop in disease_database and symptoms in disease_database[crop]:
        return {'diagnosis': symptoms, 'treatment': disease_database[crop][symptoms]}
    else:
        return {'diagnosis': 'Unknown', 'treatment': 'Consult local agricultural expert'}

# Yield prediction
def predict_yield(crop, area, N, P, K, rainfall, temperature):
    """Predict crop yield based on various factors"""
    # Simplified yield prediction model
    base_yields = {
        'Rice': 4.5,  # tons per hectare
        'Wheat': 3.5,
        'Maize': 5.0,
        'Cotton': 2.0,
        'Sugarcane': 70.0,
        'Potato': 25.0,
        'Tomato': 30.0,
        'Banana': 40.0,
        'Coffee': 1.5,
        'Tea': 2.0,
    }
    
    if crop not in base_yields:
        return {'error': 'Crop not in database'}
    
    base_yield = base_yields[crop]
    
    # Adjust yield based on nutrients (simple formula)
    nutrient_factor = min(1.2, (N + P + K) / 300)
    
    # Adjust for rainfall
    if crop in ['Rice', 'Sugarcane', 'Banana']:
        rainfall_factor = min(1.1, rainfall / 200)
    else:
        rainfall_factor = min(1.1, rainfall / 100)
    
    # Adjust for temperature
    temp_factor = 1.0
    if 20 <= temperature <= 30:
        temp_factor = 1.1
    elif temperature < 15 or temperature > 35:
        temp_factor = 0.8
    
    predicted_yield = base_yield * nutrient_factor * rainfall_factor * temp_factor
    total_production = predicted_yield * area
    
    return {
        'crop': crop,
        'area': area,
        'predicted_yield_per_hectare': round(predicted_yield, 2),
        'total_production': round(total_production, 2),
        'unit': 'tons',
        'factors': {
            'nutrient_factor': round(nutrient_factor, 2),
            'rainfall_factor': round(rainfall_factor, 2),
            'temperature_factor': round(temp_factor, 2)
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop-recommendation')
def crop_recommendation():
    return render_template('crop_recommendation.html')

@app.route('/fertilizer-recommendation')
def fertilizer_recommendation():
    return render_template('fertilizer_recommendation.html')

@app.route('/disease-prediction')
def disease_prediction():
    return render_template('disease_prediction.html')

@app.route('/yield-prediction')
def yield_prediction_page():
    return render_template('yield_prediction.html')

@app.route('/api/recommend-crop', methods=['POST'])
def api_recommend_crop():
    data = request.json
    try:
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph = float(data['ph'])
        rainfall = float(data['rainfall'])
        
        recommendations = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)
        return jsonify({'success': True, 'recommendations': recommendations})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/recommend-fertilizer', methods=['POST'])
def api_recommend_fertilizer():
    data = request.json
    try:
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        crop_type = data['crop']
        
        recommendations = recommend_fertilizer(N, P, K, crop_type)
        return jsonify({'success': True, 'recommendations': recommendations})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/predict-disease', methods=['POST'])
def api_predict_disease():
    data = request.json
    try:
        crop = data['crop']
        symptoms = data['symptoms']
        
        prediction = predict_disease(crop, symptoms)
        return jsonify({'success': True, 'prediction': prediction})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/predict-yield', methods=['POST'])
def api_predict_yield():
    data = request.json
    try:
        crop = data['crop']
        area = float(data['area'])
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        rainfall = float(data['rainfall'])
        temperature = float(data['temperature'])
        
        prediction = predict_yield(crop, area, N, P, K, rainfall, temperature)
        return jsonify({'success': True, 'prediction': prediction})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
