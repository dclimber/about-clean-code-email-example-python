from unittest import mock

from sending_mails.adapters import m_mail_client_adapter
from sending_mails.use_cases import mail_notification_interactor


class TestMailNotifications:
    def test_internal_error_is_notified_via_email(self) -> None:
        fake_mail_client = mock.Mock()
        mail_adaptor = m_mail_client_adapter.MailClientAdapter(fake_mail_client)
        interactor = mail_notification_interactor.MailNotificationInteractor(
            mock.Mock(), mock.Mock(), mail_adaptor
        )

        interactor.notify_internal_error(42, RuntimeError("Ups"))

        fake_mail_client.send.assert_called_once()
        fake_mail_send_call = fake_mail_client.mock_calls[0].args[0]
        assert "Ups" in fake_mail_send_call.body
