import dataclasses
from typing import Tuple


@dataclasses.dataclass
class InternalErrorMail:
    sender: str
    recipients: Tuple[str, ...]
    test_case: str
    error_message: str
    stack_trace: str
