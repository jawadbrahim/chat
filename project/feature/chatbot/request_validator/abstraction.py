import abc

class AbstractionRequestValidator(metaclass=abc.ABCMeta):
    def Validate_Qa(self):
        raise NotImplementedError()