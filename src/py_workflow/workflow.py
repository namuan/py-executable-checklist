import logging
import subprocess


def run_command(command: str) -> str:
    logging.info("⚡ %s", command)
    return subprocess.check_output(command, shell=True).decode("utf-8")


def notify_me(msg: str, pushover_config: dict) -> None:
    pushover_url = pushover_config["pushover_url"]
    pushover_token = pushover_config["pushover_token"]
    pushover_user = pushover_config["pushover_user"]
    if pushover_url and pushover_token and pushover_user:
        run_command(
            f"curl -s -F 'token={pushover_token}' -F 'user={pushover_user}' -F 'message={msg}' {pushover_url}"
        )


def wait_for_enter() -> None:
    input("Press Enter to continue: ")
