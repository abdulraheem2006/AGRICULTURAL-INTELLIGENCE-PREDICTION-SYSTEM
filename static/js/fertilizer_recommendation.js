document.getElementById('fertilizerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        N: document.getElementById('nitrogen').value,
        P: document.getElementById('phosphorus').value,
        K: document.getElementById('potassium').value,
        crop: document.getElementById('crop').value
    };
    
    try {
        const response = await fetch('/api/recommend-fertilizer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayRecommendations(data.recommendations);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('An error occurred: ' + error.message);
    }
});

function displayRecommendations(rec) {
    const resultsDiv = document.getElementById('results');
    const recommendationsDiv = document.getElementById('recommendations');
    
    if (rec.message) {
        recommendationsDiv.innerHTML = `
            <div class="alert alert-danger">
                ${rec.message}
            </div>
        `;
    } else {
        const hasDeficit = rec.deficit.N > 0 || rec.deficit.P > 0 || rec.deficit.K > 0;
        
        recommendationsDiv.innerHTML = `
            <div class="info-grid">
                <div class="info-item">
                    <strong>Current Nitrogen (N):</strong><br>
                    ${rec.current.N} kg/ha
                </div>
                <div class="info-item">
                    <strong>Current Phosphorus (P):</strong><br>
                    ${rec.current.P} kg/ha
                </div>
                <div class="info-item">
                    <strong>Current Potassium (K):</strong><br>
                    ${rec.current.K} kg/ha
                </div>
            </div>
            
            <div class="info-grid" style="margin-top: 1rem;">
                <div class="info-item">
                    <strong>Required Nitrogen (N):</strong><br>
                    ${rec.required.N} kg/ha
                </div>
                <div class="info-item">
                    <strong>Required Phosphorus (P):</strong><br>
                    ${rec.required.P} kg/ha
                </div>
                <div class="info-item">
                    <strong>Required Potassium (K):</strong><br>
                    ${rec.required.K} kg/ha
                </div>
            </div>
            
            <div class="recommendation-card" style="margin-top: 1.5rem;">
                <h3>Fertilizer Recommendations</h3>
                ${hasDeficit ? `
                    <div class="alert alert-warning" style="margin-top: 1rem;">
                        <strong>Nutrient Deficit Detected!</strong><br>
                        Your soil needs the following amendments:
                    </div>
                    <ul style="margin-top: 1rem; padding-left: 2rem;">
                        ${rec.recommendations.map(r => `<li>${r}</li>`).join('')}
                    </ul>
                ` : `
                    <div class="alert alert-success" style="margin-top: 1rem;">
                        ${rec.recommendations[0]}
                    </div>
                `}
            </div>
        `;
    }
    
    resultsDiv.classList.remove('hidden');
}
