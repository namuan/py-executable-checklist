import logging
import subprocess


def run_command(command: str) -> str:
    logging.info("⚡ %s", command)
    return subprocess.check_output(command, shell=True).decode("utf-8")
