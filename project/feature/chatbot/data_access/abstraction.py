import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):
    def Create_Qa(self):
        raise NotImplementedError()