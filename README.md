# Executable Workflow

[![PyPI](https://img.shields.io/pypi/v/py-executable-checklist?style=flat-square)](https://pypi.python.org/pypi/py-executable-checklist/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-executable-checklist?style=flat-square)](https://pypi.python.org/pypi/py-executable-checklist/)
[![PyPI - License](https://img.shields.io/pypi/l/py-executable-checklist?style=flat-square)](https://pypi.python.org/pypi/py-executable-checklist/)


---

**Documentation**: [https://namuan.github.io/py-executable-checklist](https://namuan.github.io/py-executable-checklist)

**Source Code**: [https://github.com/namuan/py-executable-checklist](https://github.com/namuan/py-executable-checklist)

**PyPI**: [https://pypi.org/project/py-executable-checklist/](https://pypi.org/project/py-executable-checklist/)

---

Helper classes to develop executable workflow scripts

## Installation

```sh
pip install py-executable-checklist
```

## Example Usage

```python
import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from py_executable_checklist.workflow import run_workflow, WorkflowBase


# Common functions across steps

# Workflow steps

class DoSomething(WorkflowBase):
    """
    Go to this page
    Copy the command
    Run the command
    Copy the output and paste it into the email
    """

    username: str

    def execute(self):
        logging.info(f"Hello {self.username}")

        # output
        return {"greetings": f"Hello {self.username}"}


# Workflow definition


def workflow():
    return [
        DoSomething,
    ]


# Boilerplate


def parse_args():
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-u", "--username", type=str, required=True, help="User name")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        dest="verbose",
        help="Display context variables at each step",
    )
    return parser.parse_args()


def main(args):
    context = args.__dict__
    run_workflow(context, workflow())


if __name__ == "__main__":
    args = parse_args()
    main(args)
```

## Development

* Clone this repository
* Requirements:
    * [Poetry](https://python-poetry.org/)
    * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Validating build

```sh
make build
```

### Release process

A release is automatically published when a new version is bumped using `make bump`. See `.github/workflows/build.yml`
for more details. Once the release is published, `.github/workflows/publish.yml` will automatically publish it to PyPI.
