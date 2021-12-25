from typing import Any
from unittest import mock

import pytest

from py_executable_checklist.workflow import notify_me, run_command, wait_for_enter


def test_run_command() -> None:
    cmd = "echo 'hello world'"
    run_command(cmd)


@mock.patch("subprocess.check_output")
def test_notification(mock_subprocess: Any) -> None:
    pushover_config = {
        "pushover_url": "http://localhost:8080/",
        "pushover_token": "dummy_token",
        "pushover_user": "dummy_user",
    }
    notify_me("hello world", pushover_config)

    assert mock_subprocess.called
    mock_subprocess.assert_called_with(
        "curl -s -F 'token=dummy_token' -F 'user=dummy_user' -F 'message=hello world' http://localhost:8080/",
        shell=True,
    )


def test_raise_error_if_missing_config() -> None:
    with pytest.raises(KeyError):
        notify_me("hello world", {})


@mock.patch("builtins.input")
def test_input_prompt(mock_input: Any) -> None:
    wait_for_enter()

    assert mock_input.called
    mock_input.assert_called_with("Press Enter to continue: ")
