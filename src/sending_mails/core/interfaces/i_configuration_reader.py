from abc import ABC, abstractmethod
from typing import Tuple


class IConfigurationReader(ABC):
    @abstractmethod
    def get_mail_sender(
        self,
    ) -> str:
        pass

    @abstractmethod
    def get_application_operators(self) -> Tuple[str, ...]:
        pass
