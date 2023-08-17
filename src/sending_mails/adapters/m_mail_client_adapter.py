from typing import Union

from sending_mails.adapters import html_mail
from sending_mails.adapters import i_mail_client as i_adapters_mail_client
from sending_mails.core import i_mail_client as core_mail_client
from sending_mails.core.entities import internal_error_mail, network_failure_mail


class MailClientAdapter(core_mail_client.IMailClient):
    def __init__(self, mail_client: i_adapters_mail_client.IMailClient) -> None:
        self.__mail_client: i_adapters_mail_client.IMailClient = mail_client

    def send(
        self,
        mail: Union[
            internal_error_mail.InternalErrorMail,
            network_failure_mail.NetworkFailureMail,
        ],
    ) -> None:
        method_map = {
            internal_error_mail.InternalErrorMail.__name__: self.__send_internal_error_mail,
            network_failure_mail.NetworkFailureMail.__name__: self.__send_network_failure_mail,
        }
        method_map[type(mail).__name__](mail)

    def __send_internal_error_mail(
        self, mail: internal_error_mail.InternalErrorMail
    ) -> None:
        email = html_mail.HtmlMail(
            sender=mail.sender,
            recipients=mail.recipients,
            body=self.__build_html_body(mail.error_message),
        )
        self.__mail_client.send(email)

    def __build_html_body(self, body: str) -> str:
        return f"<html><body>{body}</body></html>"

    def __send_network_failure_mail(
        self, mail: network_failure_mail.NetworkFailureMail
    ) -> None:
        pass
