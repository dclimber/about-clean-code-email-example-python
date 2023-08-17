"""Convenience APIs for "Design by Contract"."""
from typing import Iterable, TypeVar

ItemType = TypeVar("ItemType", bound=object)


class Contract:
    @staticmethod
    def requires_not_none(argument: ItemType, argument_name: str) -> None:
        """
        Ensures that the provided argument is not None.

        Args:
            argument (ItemType): The argument to check.
            argument_name (str): The name of the argument.

        Raises:
            ValueError: If the argument is None.
        """
        if argument is None:
            raise ValueError(f"{argument_name} must not be None")

    @staticmethod
    def requires_not_empty_string(argument: str, argument_name: str) -> None:
        """
        Ensures that the provided string argument is not empty.

        Args:
            argument (str): The string argument to check.
            argument_name (str): The name of the argument.

        Raises:
            ValueError: If the string argument is empty.
        """
        if not argument:
            raise ValueError(f"String must not be empty: {argument_name}")

    @staticmethod
    def requires_not_empty_collection(
        collection: Iterable[ItemType], argument_name: str
    ) -> None:
        """
        Ensures that the provided collection is not empty.

        Args:
            collection (Iterable[ItemType]): The collection to check.
            argument_name (str): The name of the argument.

        Raises:
            ValueError: If the collection is None or empty.
        """
        if collection is None:
            raise ValueError(f"{argument_name} must not be None")

        if not any(collection):
            raise ValueError(f"Collection must not be empty: {argument_name}")
