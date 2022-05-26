import logging
import os
import subprocess


def run_command(command: str) -> str:
    logging.info("⚡ %s", command)
    return subprocess.check_output(command, shell=True).decode("utf-8")  # nosemgrep


def notify_me(msg: str, pushover_config: dict) -> None:
    pushover_url = pushover_config["pushover_url"]
    pushover_token = pushover_config["pushover_token"]
    pushover_user = pushover_config["pushover_user"]
    if pushover_url and pushover_token and pushover_user:
        run_command(f"curl -s -F 'token={pushover_token}' -F 'user={pushover_user}' -F 'message={msg}' {pushover_url}")


def wait_for_enter() -> None:
    input("Press Enter to continue: ")


def __run_step(step: type, context: dict) -> None:
    step_instance = step(context, step)
    logging.info("%s ➡️ %s", step.__name__, step_instance.__doc__)
    if context.get("verbose"):
        logging.info(context)

    returned_context = step_instance.execute() or {}
    logging.info("-" * 100)
    return context.update(returned_context)


def run_workflow(context: dict, workflow_process: list) -> None:
    for step in workflow_process:
        __run_step(step, context)
    logging.info("Done.")


class WorkflowBase:
    def __init__(self, context: dict, step: type) -> None:
        has_vars = vars(step).get("__annotations__")
        if has_vars:
            step_vars = [f for f in has_vars.keys() if not f.startswith("_")]
            try:
                for step_var in step_vars:
                    setattr(self, step_var, context[step_var])
            except KeyError as e:
                error_msg = f"Unable to find variable: {str(e)}  in workflow class: {step.__name__}{os.linesep}Available keys in context: {context.keys()}"
                raise ValueError(error_msg)
