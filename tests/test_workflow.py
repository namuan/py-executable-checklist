from py_workflow.workflow import run_command


def test_run_command() -> None:
    cmd = "echo 'hello world'"
    run_command(cmd)
