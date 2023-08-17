from typing import Tuple

from sending_mails.core import i_configuration_reader


class ConfigurationReader(i_configuration_reader.IConfigurationReader):
    """Really reads configuration from somewhere: xml/json/env."""

    def get_mail_sender(
        self,
    ) -> str:
        return ""

    def get_application_operators(self) -> Tuple[str, ...]:
        return ()
