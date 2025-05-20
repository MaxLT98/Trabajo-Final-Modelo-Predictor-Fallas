import joblib
import pandas as pd
import os

class PredictorClassifier:
    def __init__(self):
        model_dir = os.path.join(os.path.dirname(__file__), 'ml-model')
        self.model = joblib.load(os.path.join(model_dir, 'model.pkl'))
        self.scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))

    def predict(self,air_temperature, process_temperature,
       rotational_speed, torque):
        new_data = pd.DataFrame([[air_temperature, process_temperature,
       rotational_speed, torque]], columns=['air_temperature','process_temperature',
       'rotational_speed', 'torque'])

        new_data_scaled = self.scaler.transform(new_data)

        prediction = self.model.predict(new_data_scaled)
        print(f"Prediction: {prediction}")
        
        return prediction[0]