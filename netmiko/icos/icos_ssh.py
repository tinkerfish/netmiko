from netmiko.cisco_base_connection import CiscoSSHConnection


class IcosSSH(CiscoSSHConnection):
    """
    Implement methods for interacting with Broadcom ICOS based devices.

    """

    def disable_paging(self, *args, **kwargs):
        """ICOS does not have paging by default"""
        return ""

    def config_mode(self, config_command="configure"):
        """Enter configuration mode."""
        return super().config_mode(config_command=config_command)

    def save_config(
        self, cmd="write memory", confirm=True, confirm_response="y",
    ):
        """Saves Config"""
        return super().save_config(
            cmd=cmd, confirm=confirm, confirm_response=confirm_response
        )
