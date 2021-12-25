# Executable Workflow

[![PyPI](https://img.shields.io/pypi/v/py-workflow?style=flat-square)](https://pypi.python.org/pypi/py-workflow/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-workflow?style=flat-square)](https://pypi.python.org/pypi/py-workflow/)
[![PyPI - License](https://img.shields.io/pypi/l/py-workflow?style=flat-square)](https://pypi.python.org/pypi/py-workflow/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://namuan.github.io/py-workflow](https://namuan.github.io/py-workflow)

**Source Code**: [https://github.com/namuan/py-workflow](https://github.com/namuan/py-workflow)

**PyPI**: [https://pypi.org/project/py-workflow/](https://pypi.org/project/py-workflow/)

---

Helper classes to develop executable workflow scripts

## Installation

```sh
pip install py-workflow
```

## Example Script

```python
#!/usr/bin/env python3
"""
Shows an example of executable documentation.

Usage:
./executable_docs.py -h

./executable_docs.py --username johndoe
"""
import argparse
import logging
from argparse import ArgumentParser

from py_workflow import run_workflow, WorkflowBase


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

    def run(self, context):
        logging.info(f"Hello {self.username}")

        # output
        context["greetings"] = f"Hello {context['username']}"


# Workflow definition


def workflow():
    return [
        DoSomething,
    ]


# Boilerplate


def parse_args():
    parser = ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
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

### Testing

```sh
pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/namuan/py-workflow/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/namuan/py-workflow/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/namuan/py-workflow/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

---

This project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
