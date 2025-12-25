# Usage Examples for AIPS

This document provides practical examples of how to use the Agricultural Intelligence Prediction System.

## Example 1: Getting Crop Recommendations

### Scenario
A farmer has a field with the following conditions:
- Nitrogen: 85 kg/ha
- Phosphorus: 45 kg/ha
- Potassium: 50 kg/ha
- Temperature: 26°C
- Humidity: 82%
- pH: 6.2
- Rainfall: 220 mm

### Solution
1. Go to the Crop Recommendation page
2. Enter the parameters
3. Get recommendations

The system will recommend crops like Rice, Sugarcane, or Maize based on suitability.

## Example 2: Fertilizer Planning

### Scenario
A farmer wants to plant Rice but has:
- Current Nitrogen: 45 kg/ha
- Current Phosphorus: 25 kg/ha
- Current Potassium: 30 kg/ha

### Solution
1. Go to Fertilizer Recommendation page
2. Select "Rice" as the crop
3. Enter current NPK values
4. Get specific fertilizer amounts needed

The system calculates:
- Nitrogen deficit: 55 kg/ha (needs 119.4 kg/ha of Urea)
- Phosphorus deficit: 25 kg/ha (needs 54.3 kg/ha of DAP)
- Potassium deficit: 20 kg/ha (needs 33.4 kg/ha of MOP)

## Example 3: Disease Diagnosis

### Scenario
A farmer notices brown spots on rice leaves.

### Solution
1. Go to Disease Prediction page
2. Select "Rice" as the crop
3. Select "Brown spots on leaves" as the symptom
4. Get diagnosis and treatment

The system identifies: Brown Spot Disease and recommends applying fungicide and improving drainage.

## Example 4: Yield Estimation

### Scenario
A farmer wants to estimate the yield for 10 hectares of Wheat with:
- Nitrogen: 65 kg/ha
- Phosphorus: 40 kg/ha
- Potassium: 40 kg/ha
- Expected rainfall: 80 mm
- Average temperature: 20°C

### Solution
1. Go to Yield Prediction page
2. Select "Wheat" and enter area (10 hectares)
3. Enter soil and weather parameters
4. Get yield estimate

The system predicts approximately 3.5 tons/hectare, totaling 35 tons for the entire field.

## API Usage Examples

### Using curl

```bash
# Crop Recommendation
curl -X POST http://localhost:5000/api/recommend-crop \
  -H "Content-Type: application/json" \
  -d '{"N":85,"P":45,"K":50,"temperature":26,"humidity":82,"ph":6.2,"rainfall":220}'

# Fertilizer Recommendation
curl -X POST http://localhost:5000/api/recommend-fertilizer \
  -H "Content-Type: application/json" \
  -d '{"N":45,"P":25,"K":30,"crop":"Rice"}'

# Disease Prediction
curl -X POST http://localhost:5000/api/predict-disease \
  -H "Content-Type: application/json" \
  -d '{"crop":"Rice","symptoms":"Brown spots on leaves"}'

# Yield Prediction
curl -X POST http://localhost:5000/api/predict-yield \
  -H "Content-Type: application/json" \
  -d '{"crop":"Wheat","area":10,"N":65,"P":40,"K":40,"rainfall":80,"temperature":20}'
```

### Using Python

```python
import requests
import json

# Crop Recommendation
response = requests.post('http://localhost:5000/api/recommend-crop',
    json={
        'N': 85,
        'P': 45,
        'K': 50,
        'temperature': 26,
        'humidity': 82,
        'ph': 6.2,
        'rainfall': 220
    })
print(json.dumps(response.json(), indent=2))
```

## Best Practices

1. **Soil Testing**: Get accurate soil tests before using the crop recommendation system
2. **Local Weather**: Use local weather forecasts for temperature, humidity, and rainfall inputs
3. **Regular Monitoring**: Check crops regularly for disease symptoms
4. **Documentation**: Keep records of recommendations and actual results
5. **Expert Consultation**: Always consult local agricultural experts for critical decisions

## Typical Workflows

### Planning Season Workflow
1. Get soil test results
2. Check weather forecast
3. Use Crop Recommendation to select suitable crops
4. Use Fertilizer Recommendation to plan nutrient requirements
5. Use Yield Prediction to estimate production
6. Plan resources and marketing accordingly

### During Growing Season Workflow
1. Monitor crops regularly
2. Use Disease Prediction if symptoms appear
3. Apply recommended treatments promptly
4. Adjust fertilizer based on crop growth
5. Update yield predictions as season progresses

## Troubleshooting

**No suitable crop found**: Your conditions may be outside optimal ranges. Try adjusting one parameter at a time to see which factors are limiting.

**Low yield predictions**: Check if nutrient levels meet requirements. Consider improving soil conditions or adjusting planting density.

**Unknown disease**: The symptom may not be in the database. Consult a local agricultural expert and consider sending a sample to a diagnostic lab.
