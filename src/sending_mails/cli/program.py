from typing import List

from sending_mails.io import (
    m_configuration_reader,
    m_mail_client,
    m_test_database_client,
)
from sending_mails.use_cases import mail_notification_interactor


def main(arguments: List[str]) -> None:
    mail_client = m_mail_client.MailClient()
    test_results_repository = m_test_database_client.TestDatabaseClient()
    config_reader = m_configuration_reader.ConfigurationReader()

    interactor = mail_notification_interactor.MailNotificationInteractor(
        config_reader, test_results_repository, mail_client
    )
