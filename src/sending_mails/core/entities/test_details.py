import dataclasses


@dataclasses.dataclass
class TestDetails:
    """
    Represents details of a test case.
    """

    id: int
    name: str
    assembly: str
