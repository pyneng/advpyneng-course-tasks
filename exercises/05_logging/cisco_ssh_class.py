import logging
from pprint import pprint
import time

import paramiko


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class CiscoSSH:
    def __init__(
        self,
        host,
        username,
        password,
        enable_password,
        max_read=60000,
        pause=0.5,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.max_read = max_read
        self.pause = pause
        log.debug(f"SSH подключение к {self.host}")

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        self._ssh = client.invoke_shell()
        self._ssh.settimeout(2)

        self._send_command("enable")
        self._send_command(enable_password)
        self._recv_output()
        self._send_command("terminal length 0")
        self._recv_output()

    def _send_command(self, command):
        self._ssh.send(f"{command}\n")

    def _recv_output(self):
        time.sleep(self.pause)
        b_output = self._ssh.recv(self.max_read)
        output = b_output.decode("utf-8").replace("\r\n", "\n")
        return output

    def send_show_command(self, command):
        log.debug(f"Отправка команды {command} на {self.host}")
        self._send_command(command)
        output = self._recv_output()
        return output

    def close(self):
        self._ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    with CiscoSSH("192.168.139.1", "cisco", "cisco", "cisco") as r1:
        out = r1.send_show_command("sh clock")
        pprint(out)
