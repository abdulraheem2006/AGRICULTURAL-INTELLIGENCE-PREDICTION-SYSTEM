const symptomsByCrop = {
    'Rice': [
        'Brown spots on leaves',
        'Yellow leaves',
        'White powdery coating'
    ],
    'Wheat': [
        'Orange pustules',
        'Yellow leaves',
        'Black spots on grains'
    ],
    'Tomato': [
        'Brown spots on leaves',
        'Curled leaves',
        'Yellow leaves'
    ],
    'Potato': [
        'Black spots on leaves',
        'Curled leaves',
        'Yellow leaves'
    ]
};

document.getElementById('crop').addEventListener('change', (e) => {
    const crop = e.target.value;
    const symptomsSelect = document.getElementById('symptoms');
    
    if (crop && symptomsByCrop[crop]) {
        symptomsSelect.innerHTML = '<option value="">-- Select Symptoms --</option>' +
            symptomsByCrop[crop].map(symptom => 
                `<option value="${symptom}">${symptom}</option>`
            ).join('');
        symptomsSelect.disabled = false;
    } else {
        symptomsSelect.innerHTML = '<option value="">-- First select a crop --</option>';
        symptomsSelect.disabled = true;
    }
});

document.getElementById('diseaseForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        crop: document.getElementById('crop').value,
        symptoms: document.getElementById('symptoms').value
    };
    
    try {
        const response = await fetch('/api/predict-disease', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const data = await response.json();
        
        if (data.success) {
            displayDiagnosis(data.prediction);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('An error occurred: ' + error.message);
    }
});

function displayDiagnosis(prediction) {
    const resultsDiv = document.getElementById('results');
    const diagnosisDiv = document.getElementById('diagnosis');
    
    diagnosisDiv.innerHTML = `
        <div class="treatment-box">
            <h3>🔍 Diagnosis</h3>
            <p><strong>${prediction.diagnosis}</strong></p>
            
            <h3 style="margin-top: 1.5rem;">💊 Treatment Recommendation</h3>
            <p>${prediction.treatment}</p>
            
            ${prediction.diagnosis === 'Unknown' ? `
                <div class="alert alert-warning" style="margin-top: 1rem;">
                    <strong>Note:</strong> This symptom is not in our database. 
                    We recommend consulting with a local agricultural expert for accurate diagnosis.
                </div>
            ` : ''}
        </div>
    `;
    
    resultsDiv.classList.remove('hidden');
}
