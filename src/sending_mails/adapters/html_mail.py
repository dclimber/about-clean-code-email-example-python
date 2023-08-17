from typing import Tuple


class HtmlMail:
    def __init__(self, sender: str, recipients: Tuple[str, ...], body: str) -> None:
        self.__sender: str = sender
        self.__recipients: Tuple[str, ...] = recipients
        self.__body: str = body

    @property
    def sender(self) -> str:
        return self.__sender

    @property
    def recipients(self) -> Tuple[str, ...]:
        return self.__recipients

    @property
    def body(self) -> str:
        return self.__body
