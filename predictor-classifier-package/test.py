from predictor_classifier import PredictorClassifier

classifier = PredictorClassifier()

air_temperature = 310
process_temperature = 315.6
rotational_speed = 1540
torque = 43.1

prediction = classifier.predict(air_temperature, process_temperature, rotational_speed, torque)
print(f"Prediction: {prediction}")