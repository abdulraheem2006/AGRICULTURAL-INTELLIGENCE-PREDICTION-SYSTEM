# 🌾 Agricultural Intelligence Prediction System (AIPS)

Agricultural Intelligence Prediction System (AIPS) is an AI-driven web application that helps farmers make smarter, data-based farming decisions. It addresses key agricultural challenges such as unpredictable weather, poor soil quality, inefficient use of land and water resources, and fluctuating market prices.

## 🚀 Features

### 1. Crop Recommendation System
- Recommends the most suitable crops based on soil nutrients (NPK values)
- Considers environmental factors like temperature, humidity, pH, and rainfall
- Provides suitability percentage for each recommended crop
- Supports 10+ major crops including Rice, Wheat, Maize, Cotton, Sugarcane, and more

### 2. Fertilizer Recommendation
- Calculates optimal fertilizer requirements based on current soil nutrient levels
- Provides specific recommendations for Nitrogen (Urea), Phosphorus (DAP), and Potassium (MOP)
- Customized recommendations for different crop types
- Helps optimize fertilizer usage and reduce costs

### 3. Crop Disease Prediction
- Identifies crop diseases based on visible symptoms
- Provides treatment recommendations and preventive measures
- Covers common diseases for Rice, Wheat, Tomato, and Potato
- Early detection helps minimize crop losses

### 4. Yield Prediction
- Estimates crop yield based on multiple factors
- Considers soil nutrients, weather conditions, and cultivated area
- Provides both per-hectare and total production estimates
- Helps in planning and resource allocation

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/abdulraheem2006/AGRICULTURAL-INTELLIGENCE-PREDICTION-SYSTEM.git
cd AGRICULTURAL-INTELLIGENCE-PREDICTION-SYSTEM
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. The application will be running on port 5000 by default.

## 💻 Usage

### Crop Recommendation
1. Navigate to the "Crop Recommendation" page
2. Enter soil parameters:
   - Nitrogen (N) content in kg/ha
   - Phosphorus (P) content in kg/ha
   - Potassium (K) content in kg/ha
3. Enter environmental parameters:
   - Temperature in Celsius
   - Humidity percentage
   - pH level of soil
   - Expected rainfall in mm
4. Click "Get Recommendations" to see suitable crops with suitability scores

### Fertilizer Recommendation
1. Navigate to the "Fertilizer Recommendation" page
2. Select your crop from the dropdown
3. Enter current soil nutrient levels (N, P, K)
4. Click "Get Recommendations" to see fertilizer requirements

### Disease Prediction
1. Navigate to the "Disease Prediction" page
2. Select your crop
3. Choose the observed symptoms from the dropdown
4. Click "Diagnose Disease" to get diagnosis and treatment recommendations

### Yield Prediction
1. Navigate to the "Yield Prediction" page
2. Select the crop and enter cultivated area
3. Enter soil parameters and weather conditions
4. Click "Predict Yield" to see estimated production

## 📊 Data

The system uses a comprehensive database of:
- Crop nutrient requirements
- Disease symptoms and treatments
- Base yield data for different crops
- Optimal growing conditions

Sample data is available in the `data/` directory.

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: Scikit-learn (ready for ML model integration)

## 🌟 Key Benefits

- ✅ Data-driven decision making for farmers
- ✅ Optimized resource utilization (water, fertilizer, land)
- ✅ Early disease detection and prevention
- ✅ Increased crop yield and profitability
- ✅ Reduced environmental impact through efficient resource use
- ✅ User-friendly interface accessible to farmers with basic technical knowledge

## 🔮 Future Enhancements

- Integration with real-time weather APIs
- Machine learning models for more accurate predictions
- Mobile application for field access
- Multi-language support for regional languages
- Image-based disease detection using computer vision
- Market price prediction and forecasting
- Integration with IoT sensors for real-time soil monitoring

## 📝 API Endpoints

- `POST /api/recommend-crop` - Get crop recommendations
- `POST /api/recommend-fertilizer` - Get fertilizer recommendations
- `POST /api/predict-disease` - Predict crop disease
- `POST /api/predict-yield` - Predict crop yield

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👥 Authors

- Agricultural Intelligence Prediction System Team

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Note**: This system provides estimates and recommendations based on general agricultural data. Always consult with local agricultural experts for critical farming decisions.
