# Agricultural Intelligence Prediction System - Quick Reference

## 🌾 System Overview

AIPS is a comprehensive agricultural decision support system with four main modules:

### 1. Crop Recommendation 🌱
**Purpose**: Find the best crop for your soil and climate conditions  
**Inputs**: N, P, K, Temperature, Humidity, pH, Rainfall  
**Output**: List of suitable crops with suitability percentage  

### 2. Fertilizer Recommendation 💧
**Purpose**: Calculate exact fertilizer needs for your crop  
**Inputs**: Current NPK levels, Crop type  
**Output**: Required amounts of Urea, DAP, and MOP  

### 3. Disease Prediction 🔬
**Purpose**: Diagnose crop diseases from symptoms  
**Inputs**: Crop type, Observed symptoms  
**Output**: Disease diagnosis and treatment recommendations  

### 4. Yield Prediction 📊
**Purpose**: Estimate crop production for planning  
**Inputs**: Crop, Area, NPK, Rainfall, Temperature  
**Output**: Expected yield per hectare and total production  

## 📏 Parameter Ranges

### Soil Nutrients
- **Nitrogen (N)**: 0-200 kg/ha
- **Phosphorus (P)**: 0-150 kg/ha
- **Potassium (K)**: 0-300 kg/ha
- **pH**: 0-14 (typically 4.5-8.0 for agriculture)

### Environmental
- **Temperature**: 0-50°C (typically 15-35°C for crops)
- **Humidity**: 0-100%
- **Rainfall**: 0-500 mm per season

## 🌾 Supported Crops

1. **Rice** - High water requirement, tropical/subtropical
2. **Wheat** - Moderate water, temperate climate
3. **Maize (Corn)** - Moderate water, warm climate
4. **Cotton** - Low-moderate water, warm climate
5. **Sugarcane** - High water, tropical climate
6. **Potato** - Moderate water, cool climate
7. **Tomato** - Moderate water, warm climate
8. **Banana** - High water, tropical climate
9. **Coffee** - High rainfall, cool-warm climate
10. **Tea** - High rainfall, acidic soil preference

## 🔢 Typical NPK Requirements by Crop

| Crop      | N (kg/ha) | P (kg/ha) | K (kg/ha) |
|-----------|-----------|-----------|-----------|
| Rice      | 80-120    | 40-60     | 40-60     |
| Wheat     | 50-80     | 30-50     | 30-50     |
| Maize     | 60-100    | 40-60     | 40-60     |
| Cotton    | 60-100    | 30-50     | 30-50     |
| Sugarcane | 80-150    | 40-80     | 60-100    |
| Potato    | 50-80     | 50-80     | 50-80     |
| Tomato    | 40-70     | 40-70     | 40-70     |
| Banana    | 100-200   | 50-100    | 150-300   |
| Coffee    | 60-100    | 30-50     | 60-100    |
| Tea       | 80-120    | 40-60     | 40-60     |

## 🦠 Common Diseases Covered

### Rice
- Brown Spot Disease
- Blast Disease  
- Nitrogen deficiency

### Wheat
- Rust Disease
- Smut Disease
- Nutrient deficiencies

### Tomato
- Early Blight
- Virus infections
- Nutrient deficiencies

### Potato
- Late Blight
- Leaf Roll Virus
- Nutrient deficiencies

## 📱 API Endpoints

```
POST /api/recommend-crop
POST /api/recommend-fertilizer
POST /api/predict-disease
POST /api/predict-yield
```

## 🚀 Quick Start Commands

```bash
# Install
pip install -r requirements.txt

# Run Tests
python test_system.py

# Start Server
python app.py

# Access Application
http://localhost:5000
```

## 💡 Tips for Best Results

1. **Accurate Soil Testing**: Get professional soil tests for NPK and pH
2. **Local Weather Data**: Use accurate local weather forecasts
3. **Season Timing**: Consider planting seasons for your region
4. **Crop Rotation**: Plan crop rotation for soil health
5. **Expert Advice**: Consult local agricultural extension officers
6. **Record Keeping**: Document results to improve future predictions

## ⚠️ Important Notes

- Results are estimates based on general agricultural data
- Local conditions may vary significantly
- Always consult agricultural experts for critical decisions
- Soil and weather conditions should be monitored regularly
- Disease symptoms should be confirmed by experts when possible

## 📞 Support

- Documentation: README.md
- Examples: USAGE_EXAMPLES.md
- Deployment: DEPLOYMENT.md
- Issues: GitHub Issues

## 🔐 System Requirements

- Python 3.7+
- Modern web browser (Chrome, Firefox, Safari, Edge)
- 512MB RAM minimum (1GB recommended)
- Internet connection for initial setup

## 📈 Performance

- Response time: < 1 second per prediction
- Concurrent users: 100+ (with proper deployment)
- Scalability: Horizontal scaling supported
- Uptime: 99%+ (with proper infrastructure)
