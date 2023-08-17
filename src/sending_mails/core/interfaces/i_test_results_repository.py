from abc import ABC, abstractmethod

from sending_mails.core.entities import test_details


class ITestResultsRepository(ABC):
    """Interface for accessing test results repository."""

    @abstractmethod
    def get_test_details(self, test_case_id: int) -> test_details.TestDetails:
        """
        Retrieve test details for the given test case ID.

        Args:
            test_case_id (int): The ID of the test case.

        Returns:
            TestDetails: Test details object.
        """
        pass
