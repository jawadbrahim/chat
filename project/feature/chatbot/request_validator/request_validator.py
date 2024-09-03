
from .abstraction import AbstractionRequestValidator
from .request_validator_models import Chat_Bot_Model
from project.decorator.validate import validate_schema

class ChatBotValidtor(AbstractionRequestValidator):
    def Validate_Qa(self):
        return validate_schema(json_schema=Chat_Bot_Model)
