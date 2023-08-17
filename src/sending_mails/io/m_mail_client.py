from sending_mails.adapters import html_mail, i_mail_client


class MailClient(i_mail_client.IMailClient):
    """Actually sends the email."""

    def send(self, mail: html_mail.HtmlMail) -> None:
        pass
