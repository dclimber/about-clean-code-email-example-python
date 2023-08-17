from abc import ABC, abstractmethod

from sending_mails.adapters import html_mail


class IMailClient(ABC):
    @abstractmethod
    def send(self, mail: html_mail.HtmlMail) -> None:
        pass
