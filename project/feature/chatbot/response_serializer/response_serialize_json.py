from .abstraction import AbstarctionResponseSeraizlier
from .response_model import SerailzeModel
from ..data_classes import Create_Qa
class Response_json(AbstarctionResponseSeraizlier):
    def Serialize_ChatBot(self,qa):
        qa_data=Create_Qa(
            id=qa.id,
            question=qa.question,
            answer=qa.answer,
            created_at=qa.created_at
        )
        response=SerailzeModel(qa=qa_data)
        return response.json()
        