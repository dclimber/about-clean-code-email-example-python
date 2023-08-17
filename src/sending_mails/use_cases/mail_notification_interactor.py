import traceback
from typing import Type

from sending_mails.core.entities import internal_error_mail, network_failure_mail
from sending_mails.core.interfaces import (
    i_configuration_reader,
    i_mail_client,
    i_test_results_repository,
)


class MailNotificationInteractor:
    def __init__(
        self,
        config_reader: i_configuration_reader.IConfigurationReader,
        test_result_repository: i_test_results_repository.ITestResultsRepository,
        mail_client: i_mail_client.IMailClient,
    ) -> None:
        self.__config_reader: i_configuration_reader.IConfigurationReader = (
            config_reader
        )
        self.__test_result_repository: i_test_results_repository.ITestResultsRepository = (
            test_result_repository
        )
        self.__mail_client: i_mail_client.IMailClient = mail_client

    def notify_internal_error(
        self, test_case_id: int, exception: Type[Exception]
    ) -> None:
        string_traceback: str = "".join(traceback.format_exception(exception))
        mail: internal_error_mail.InternalErrorMail = (
            internal_error_mail.InternalErrorMail(
                sender=self.__config_reader.get_mail_sender(),
                recipients=self.__config_reader.get_application_operators(),
                error_message=str(exception),
                stack_trace=string_traceback,
                test_case=self.__test_result_repository.get_test_details(
                    test_case_id
                ).name,
            )
        )
        self.__mail_client.send(mail)

    def check_missing_test_cases(self, build_id: str) -> None:
        # some more business logic goes here to detect
        # that there was a network issue
        mail: network_failure_mail.NetworkFailureMail = (
            network_failure_mail.NetworkFailureMail(
                sender=self.__config_reader.get_mail_sender(),
                recipients=self.__config_reader.get_application_operators(),
                build_id=build_id,
                test_agents=(),
            )
        )
        self.__mail_client.send(mail)
