import abc

class AbstractionService(metaclass=abc.ABCMeta):
    def Create_Qa(self):
        raise NotImplementedError()