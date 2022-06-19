from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self,nome: str , email: str):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @email.setter
    def email(self, email):
        self.__email = email

