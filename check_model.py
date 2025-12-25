
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'backend', 'models', 'yield_model.pkl')

if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, 'rb') as f:
            data = pickle.load(f)
            perf = data.get('performance', {})
            print(f"R2 Score: {perf.get('r2')}")
            
            # Check estimators
            model = data.get('model')
            if hasattr(model, 'estimators_'):
                print(f"Estimators available: {len(model.estimators_)}")
            else:
                print("Estimators NOT available")
                
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"Model not found at {MODEL_PATH}")
