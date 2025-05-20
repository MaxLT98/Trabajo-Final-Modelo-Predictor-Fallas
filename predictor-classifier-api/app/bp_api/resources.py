from flask_restful import Resource, Api
from flask import request   
from . import bp_api
from.models import Predictor
from .schemas import PredictorSchema

api = Api(bp_api)

class ApiResource(Resource):
    def get(self):

        data = Predictor.get_all()
        predictor_schema = PredictorSchema(many=True)

        context = {
            'status': True,
            'message': 'Lista de Registros',
            'content': predictor_schema.dump(data)
        }
        return context, 200
    
    def post(self):
        data = request.get_json()
        if not data:
            return {'status': False, 'message': 'No data provided'}, 400
        
        air_temperature = data.get('air_temperature')
        process_temperature = data.get('process_temperature')
        rotational_speed = data.get('rotational_speed')
        torque = data.get('torque')

        predictor = Predictor(air_temperature=air_temperature,process_temperature=process_temperature,rotational_speed=rotational_speed,torque=torque)
        predictor.save()

        predictor_schema = PredictorSchema()

        try:
            context = {
                'status': True,
                'message': 'Registro Creado',
                'content': predictor_schema.dump(predictor)
            }
            return context, 201
        
        except Exception as e:
            return {'status': False, 'message': str(e)}, 500
    
api.add_resource(ApiResource, '/')