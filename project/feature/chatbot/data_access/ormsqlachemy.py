from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import Orm
from project.model.qa import Qa
from ..data_classes import Create_Qa


class OrmSqlachemy(AbstractionDataAccess,Orm):
    def form_qa(self,qa):

        return Create_Qa(
            id=qa.id,
            question=qa.question,
            answer=qa.answer,
            created_at=qa.created_at
        )
        
    def Create_Qa(self,question,answer):
        qa=Qa(
            question=question,
            answer=answer


        )
        self.add(qa)
        return qa


        
        