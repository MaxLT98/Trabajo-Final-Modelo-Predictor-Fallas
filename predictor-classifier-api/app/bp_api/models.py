from utils.db import db
from predictor_classifier import PredictorClassifier

class Predictor(db.Model):
    __tablename__ = 'predictor'
    id = db.Column(db.Integer, primary_key=True)
    air_temperature = db.Column(db.Double, primary_key=False)
    process_temperature = db.Column(db.Double, primary_key=False)
    rotational_speed = db.Column(db.Integer, primary_key=False)
    torque = db.Column(db.Double, primary_key=False)
    is_fail = db.Column(db.Boolean, nullable=False)

    def __init__(self, air_temperature, process_temperature, rotational_speed, torque):
        self.air_temperature = air_temperature
        self.process_temperature = process_temperature
        self.rotational_speed = rotational_speed
        self.torque = torque

    @staticmethod
    def get_all():
        return Predictor.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Predictor.query.get(id)


    def save(self):
        ml_predictor = PredictorClassifier()
        self.is_fail = ml_predictor.predict(self.air_temperature, self.process_temperature, self.rotational_speed, self.torque)
        db.session.add(self)
        db.session.commit()