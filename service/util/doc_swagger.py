# -*- coding: utf-8 -*-
from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'mes': fields.List(fields.String(), required=True, description= "Mes do nascimento"),
    'dia': fields.List(fields.Integer(), required=True, description= "Dia do nascimento")})
