document.getElementById('cropForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        N: document.getElementById('nitrogen').value,
        P: document.getElementById('phosphorus').value,
        K: document.getElementById('potassium').value,
        temperature: document.getElementById('temperature').value,
        humidity: document.getElementById('humidity').value,
        ph: document.getElementById('ph').value,
        rainfall: document.getElementById('rainfall').value
    };
    
    try {
        const response = await fetch('/api/recommend-crop', {
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

function displayRecommendations(recommendations) {
    const resultsDiv = document.getElementById('results');
    const recommendationsDiv = document.getElementById('recommendations');
    
    if (recommendations.length === 0 || recommendations[0].suitability === 0) {
        recommendationsDiv.innerHTML = `
            <div class="alert alert-warning">
                <strong>No suitable crops found!</strong><br>
                The provided soil and environmental conditions do not match our crop requirements database.
                Please verify your inputs or consult with a local agricultural expert.
            </div>
        `;
    } else {
        recommendationsDiv.innerHTML = recommendations.map(rec => `
            <div class="recommendation-card">
                <h3>${rec.crop}</h3>
                <p>Suitability: ${rec.suitability}%</p>
                <div class="suitability-bar">
                    <div class="suitability-fill" style="width: ${rec.suitability}%"></div>
                </div>
            </div>
        `).join('');
    }
    
    resultsDiv.classList.remove('hidden');
}
