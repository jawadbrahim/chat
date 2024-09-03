from ..setting.options import RequestValidtorOption
from ..setting.development import Development
from .request_validator import ChatBotValidtor

class FactoryRequestValidator:
    @staticmethod
    def build_object(service=Development.REQUST_VALIDTOR):
        if service == RequestValidtorOption.REUQEST_MODEL:
            return ChatBotValidtor()
        raise NotImplementedError()
