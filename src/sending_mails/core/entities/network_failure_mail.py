import dataclasses
from typing import Tuple


@dataclasses.dataclass
class NetworkFailureMail:
    sender: str
    recipients: Tuple[str, ...]
    build_id: str
    test_agents: Tuple[str, ...]
