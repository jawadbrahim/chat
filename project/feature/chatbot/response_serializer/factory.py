
from ..setting.options import SerializeOption
from ..setting.development import Development
from .response_serialize_json import Response_json

class FactoryResponseSerializer():
    @staticmethod
    def build_object(service=Development.SERIALIZE):
        if service == SerializeOption.PYDANTIC_JSON:
            return Response_json()
        raise NotImplementedError()