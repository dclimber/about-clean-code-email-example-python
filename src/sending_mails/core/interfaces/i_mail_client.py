from abc import ABC, abstractmethod
from typing import Union

from sending_mails.core.entities import internal_error_mail, network_failure_mail


class IMailClient(ABC):
    @abstractmethod
    def send(
        self,
        mail: Union[
            internal_error_mail.InternalErrorMail,
            network_failure_mail.NetworkFailureMail,
        ],
    ) -> None:
        pass
