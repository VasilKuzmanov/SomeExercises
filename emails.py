from __future__ import annotations
from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self) -> type[IContent: str]:
        ...


class MyMl(IContent):

    def format(self) -> type[IContent: str]:
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):

    def format(self) -> type[IContent: str]:
        return '\n'.join(['<html>', self.text, '</html>'])


class IEmail(ABC):

    @staticmethod
    @abstractmethod
    def sender(sender: str) -> str:
        return sender

    @staticmethod
    @abstractmethod
    def receiver(receiver: str) -> str:
        return receiver


class IM(IEmail):

    @staticmethod
    def sender(sender: str) -> str:
        return ''.join(["from ", sender])

    @staticmethod
    def receiver(receiver: str) -> str:
        return ''.join(["to ", receiver])


class Email:

    def __init__(self, template: type[IEmail]):
        self.__template = template
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: str) -> None:
        self.__sender = self.__template.sender(sender)

    def set_receiver(self, receiver: str) -> None:
        self.__receiver = self.__template.receiver(receiver)

    def set_content(self, content: IContent) -> None:
        self.__content = content.format()

    def __repr__(self) -> str:
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


myml = MyMl('Hello, there!')
email = Email(IEmail)
email.set_sender('Ivan')
email.set_receiver('James')
email.set_content(myml)

print(email)
print()

myml2 = HTML('Hello, there!')
email = Email(IM)
email.set_sender('Ivan')
email.set_receiver('James')
email.set_content(myml2)

print(email)