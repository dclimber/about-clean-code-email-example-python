from typing import Union

from sending_mails.core import i_mail_client
from sending_mails.core.entities import internal_error_mail, network_failure_mail


class MailClient(i_mail_client.IMailClient):
    """Actually sends the email."""

    def send(
        self,
        mail: Union[
            internal_error_mail.InternalErrorMail,
            network_failure_mail.NetworkFailureMail,
        ],
    ) -> None:
        pass
