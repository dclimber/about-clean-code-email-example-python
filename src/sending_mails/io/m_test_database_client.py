from sending_mails.core import i_test_results_repository
from sending_mails.core.entities import test_details


class TestDatabaseClient(i_test_results_repository.ITestResultsRepository):
    """Accesses some real database to get some data from it."""

    def get_test_details(self, test_case_id: int) -> test_details.TestDetails:
        return test_details.TestDetails(0, "", "")
