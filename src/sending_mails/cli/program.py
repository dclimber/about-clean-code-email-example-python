from typing import List

from sending_mails.adapters import i_mail_client as adapter_i_mail_client
from sending_mails.adapters import m_mail_client_adapter
from sending_mails.io import (
    m_configuration_reader,
    m_mail_client,
    m_test_database_client,
)
from sending_mails.use_cases import mail_notification_interactor


def main(arguments: List[str]) -> None:
    # initiate drivers
    mail_client: adapter_i_mail_client.IMailClient = m_mail_client.MailClient()
    test_results_repository: m_test_database_client.TestDatabaseClient = (
        m_test_database_client.TestDatabaseClient()
    )
    config_reader: m_configuration_reader.ConfigurationReader = (
        m_configuration_reader.ConfigurationReader()
    )

    # initiate html mail adapter
    mail_client_adapter: m_mail_client_adapter.MailClientAdapter = (
        m_mail_client_adapter.MailClientAdapter(mail_client)
    )

    # start the use case
    interactor: mail_notification_interactor.MailNotificationInteractor = (
        mail_notification_interactor.MailNotificationInteractor(
            config_reader, test_results_repository, mail_client_adapter
        )
    )
