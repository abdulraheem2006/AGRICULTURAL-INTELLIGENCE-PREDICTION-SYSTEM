document.getElementById('yieldForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        crop: document.getElementById('crop').value,
        area: document.getElementById('area').value,
        N: document.getElementById('nitrogen').value,
        P: document.getElementById('phosphorus').value,
        K: document.getElementById('potassium').value,
        rainfall: document.getElementById('rainfall').value,
        temperature: document.getElementById('temperature').value
    };
    
    try {
        const response = await fetch('/api/predict-yield', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayPrediction(data.prediction);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('An error occurred: ' + error.message);
    }
});

function displayPrediction(pred) {
    const resultsDiv = document.getElementById('results');
    const predictionDiv = document.getElementById('prediction');
    
    if (pred.error) {
        predictionDiv.innerHTML = `
            <div class="alert alert-danger">
                ${pred.error}
            </div>
        `;
    } else {
        predictionDiv.innerHTML = `
            <div class="recommendation-card">
                <h3>📈 Yield Prediction for ${pred.crop}</h3>
                
                <div class="info-grid" style="margin-top: 1.5rem;">
                    <div class="info-item">
                        <strong>Cultivated Area:</strong><br>
                        ${pred.area} hectares
                    </div>
                    <div class="info-item">
                        <strong>Yield per Hectare:</strong><br>
                        ${pred.predicted_yield_per_hectare} ${pred.unit}
                    </div>
                    <div class="info-item">
                        <strong>Total Production:</strong><br>
                        ${pred.total_production} ${pred.unit}
                    </div>
                </div>
                
                <div style="margin-top: 1.5rem;">
                    <h4>Factors Affecting Yield:</h4>
                    <div class="info-grid" style="margin-top: 1rem;">
                        <div class="info-item">
                            <strong>Nutrient Factor:</strong><br>
                            ${pred.factors.nutrient_factor}x
                        </div>
                        <div class="info-item">
                            <strong>Rainfall Factor:</strong><br>
                            ${pred.factors.rainfall_factor}x
                        </div>
                        <div class="info-item">
                            <strong>Temperature Factor:</strong><br>
                            ${pred.factors.temperature_factor}x
                        </div>
                    </div>
                </div>
                
                <div class="alert alert-success" style="margin-top: 1.5rem;">
                    <strong>Note:</strong> This is an estimated yield based on the provided parameters. 
                    Actual yield may vary depending on other factors such as pest management, 
                    irrigation practices, and crop variety.
                </div>
            </div>
        `;
    }
    
    resultsDiv.classList.remove('hidden');
}
