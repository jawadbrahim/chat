from ..setting.options import OrmSqlalchemyOption
from ..setting.development import Development
from .ormsqlachemy import OrmSqlachemy


class FactoryDataAccess:
    @staticmethod
    def build_object(service=Development.ORM_SQLACHEMY):
        if service == OrmSqlalchemyOption.ORMSQLACHEMY:
            return OrmSqlachemy()
        raise NotImplementedError()