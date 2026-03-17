import requests

from model.http.engine.EngineModel import AbstractEngine
from model.http.info.ContentModel import ResponseContent
from model.http.info.MethodModel import AbstractHttpMethod


class StandardEngine:
    def __init__(self):
        super().__init__()
