from __future__ import annotations

from typing import Any, Optional
from unittest import mock

import pytest

from py_executable_checklist.workflow import (
    WorkflowBase,
    notify_me,
    run_command,
    run_workflow,
    wait_for_enter,
)


def test_run_command() -> None:
    cmd = "echo 'hello world'"
    run_command(cmd)


@mock.patch("subprocess.check_output")
def test_send_notification(mock_subprocess: Any) -> None:
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


def test_raise_error_for_missing_config() -> None:
    with pytest.raises(KeyError):
        notify_me("hello world", {})


@mock.patch("builtins.input")
def test_wait_for_user_input(mock_input: Any) -> None:
    wait_for_enter()

    assert mock_input.called
    mock_input.assert_called_with("Press Enter to continue: ")


def test_run_workflow_with_context() -> None:
    context = {
        "username": "dummy_user",
        "verbose": True,
    }

    class SimpleStep(WorkflowBase):
        """Step documentation"""

        username: str  # automatically set by the workflow

        def execute(self) -> None:
            pass

    workflow_steps = [SimpleStep]

    run_workflow(context, workflow_steps)

    assert context.get("ret_value") is None
    assert context.get("username") == "dummy_user"


def test_run_workflow_update_returned_context() -> None:
    context = {"username": "dummy_user"}

    class SimpleStep(WorkflowBase):
        """Step documentation"""

        username: str  # automatically set by the workflow

        def execute(self) -> Optional[dict]:
            # This returned value will be merged into the context
            return {"ret_value": f"Hello {self.username}"}

    workflow_steps = [SimpleStep]

    run_workflow(context, workflow_steps)

    assert context["ret_value"] == "Hello dummy_user"


def test_raise_error_for_missing_variable() -> None:
    context = {
        "verbose": True,
    }

    class MissingVariableToMapStep(WorkflowBase):
        verbose: bool
        missing_var: str  # missing in context so will raise an error

    workflow_steps = [MissingVariableToMapStep]

    with pytest.raises(ValueError):
        run_workflow(context, workflow_steps)


def test_ignore_private_variables() -> None:
    class PrivateVariableStep(WorkflowBase):
        _this_is_a_private_var: str

        def execute(self) -> None:
            pass

    workflow_steps = [PrivateVariableStep]

    run_workflow({}, workflow_steps)


def test_support_for_sub_workflows() -> None:
    context: dict = {}

    class ChildWorkflowStep1(WorkflowBase):
        def execute(self) -> dict:
            return {"child1": "Child 1 was here"}

    class ChildWorkflowStep2(WorkflowBase):
        child1: str

        def execute(self) -> dict:
            return {"child2": self.child1 + ", Child 2 was here too"}

    class ParentWorkflowStep(WorkflowBase):
        def execute(self) -> None:
            sub_workflow_steps = [ChildWorkflowStep1, ChildWorkflowStep2]
            run_workflow(self.context, sub_workflow_steps)

    workflow_steps = [ParentWorkflowStep]
    run_workflow(context, workflow_steps)

    assert context["child1"] == "Child 1 was here"
    assert context["child2"] == "Child 1 was here, Child 2 was here too"
