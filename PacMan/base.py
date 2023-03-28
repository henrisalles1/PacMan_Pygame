from abc import ABCMeta, abstractmethod


class Element(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcula_regra(self):
        pass

    @abstractmethod
    def processa_evento(self, eventos):
        pass

class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceita_movimento(self):
        pass

    @abstractmethod
    def recusa_movimento(self, direcoes):
        pass

    @abstractmethod
    def esquina(self, direcoes):
        pass
