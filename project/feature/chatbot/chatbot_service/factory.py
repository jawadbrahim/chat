from ..setting.options import ServiceOption
from ..setting.development import Development

from .default import Default


class FactoryChatBotService():
    @staticmethod
    def build_object(data_access,service=Development.CHAT_BOT):
        if service == ServiceOption.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()