from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Predictor

class PredictorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Predictor