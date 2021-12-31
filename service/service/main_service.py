# -*- coding: utf-8 -*-
import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np

class SignoService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o horoscopo
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):

        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts = self.buscar_signo(texts['mes'], texts['dia'])
        

        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")
        response = {
                    "Signo": response_predicts}

        return response

    def buscar_signo(self, mes, day):
        """
        Pega o modelo carregado e aplica em texts
        """
        logger.debug('Iniciando a classificacao do signo..')
        

        response = []


        for d, texts in zip(day,mes):
            dia = int(d)
            if texts == 'janeiro':
                if dia <= 20:
                    response.append('Capricornio')
                elif dia >= 21 and dia < 31:
                    response.append('Aquario')
            if texts == 'fevereiro':
                if dia <= 18:
                    response.append('Aquario')
                elif dia >= 19 and dia < 31:
                    response.append('Peixes')
            if texts == 'marco':
                if dia <= 20:
                    response.append('Peixes')
                elif dia >=21:
                    response.append('Aries')
            if texts == 'abril':
                if dia <= 20:
                    response.append('Aries')
                elif dia >=21:
                    response.append('Touros')
            if texts == 'maio':
                if dia <= 20:
                    response.append('Touro')
                elif dia >=21:
                    response.append('Gemeos')
            if texts == 'junho':
                if dia <= 20:
                    response.append('Gemeos')
                elif dia >=21:
                    response.append('Cancer')
            if texts == 'julho':
                if dia <= 22:
                    response.append('Cancer')
                elif dia >=23:
                    response.append('Leao')
            if texts == 'agosto':
                if dia <= 22:
                    response.append('Leao')
                elif dia >=23:
                    response.append('Virgem')
            if texts == 'setembro':
                if dia <= 22:
                    response.append('Virgem')
                elif dia >=23:
                    response.append('Libra')
            if texts == 'outubro':
                if dia <= 22:
                    response.append('Libra')
                elif dia >=23:
                    response.append('Escorpiao')
            if texts == 'novembro':
                if dia <= 21:
                    response.append('Escorpiao')
                elif dia >=22:
                    response.append('Sagitario')
            if texts == 'dezembro':
                if dia <= 21:
                    response.append('Sagitario')
                elif dia >=22:
                    response.append('Capricornio')
            elif dia > 31:
                response.append('Dia Invalido')
            else:
                response.append('Mes invalido')

            
        return response