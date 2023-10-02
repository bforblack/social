import grpc
from protobufs import nlpengine_pb2_grpc
from protobufs import nlpengine_pb2

import os
import logging
import requests


class NLPService:
    def __init__(self):
        self.nlp_engine_endpoint = os.getenv('NLP_ENGINE')
        self.zero_shots_endpoint = os.getenv('Zero_shots')

    def sentiment(self, message):
        try:
            channel = grpc.insecure_channel(self.nlp_engine_endpoint)
            stub = nlpengine_pb2_grpc.NLPEngineStub(channel)
            call = stub.Sentiment(nlpengine_pb2.RequestMessage(text=message))
            return call
        except Exception as ex:
            logging.error(f"Sentiment API call failed: {ex}")
            return None

    def name_entity_recognition(self, sentence_list, intent_list):
        url = self.zero_shots_endpoint + '/Zero-Shot-Data-Tagging'
        data = {
            "summaries": sentence_list,
            "intent_labels": intent_list
        }

        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                response_json = response.json()
                intent = response_json.get('intents')
                entities = response_json.get('entities')
                return intent, entities
            else:
                logging.error(f"Request failed with status code: {response.status_code}")
                return None, None
        except Exception as ex:
            logging.error(f"API call failed: {ex}")
            return None, None
