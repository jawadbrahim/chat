import abc

class AbstarctionResponseSeraizlier(metaclass=abc.ABCMeta):

    def Serialize_ChatBot(self):
        raise NotImplementedError()