# Mokkari

[![Version](https://img.shields.io/pypi/v/mokkari.svg?logo=PyPI&label=Version&style=flat-square)](https://pypi.org/project/mokkari)
![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9-green?style=flat-square)
[![License](https://img.shields.io/github/license/bpepple/mokkari)](https://opensource.org/licenses/GPL-3.0)

[![Hatch](https://img.shields.io/badge/Packaging-Hatch-4051b5?style=flat-square)](https://github.com/pypa/hatch)
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-Enabled-informational?style=flat-square&logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/badge/Linter-Ruff-informational?style=flat-square)](https://github.com/astral-sh/ruff)
[![Ruff](https://img.shields.io/badge/Formatter-Ruff-informational?style=flat-square)](https://github.com/astral-sh/ruff)

## Quick Description

A python wrapper for the [metron.cloud](https://metron.cloud) API.

## Installation

### PyPi

```bash
$ pip3 install --user mokkari
```

## Example Usage

```python
import mokkari
from config import username, password

m = mokkari.api(username, password)

# Get all Marvel comics for the week of 2021-06-07
this_week = m.issues_list({"store_date_range_after": "2021-06-07", "store_date_range_before": "2021-06-13", "publisher_name": "marvel"})

# Print the results
for i in this_week:
    print(f"{i.id} {i.issue_name}")

# Retrieve the detail for an individual issue
asm_68 = m.issue(31660)

# Print the issue Description
print(asm_68.desc)
```

## Documentation

- [Read the project documentation](https://mokkari.readthedocs.io/en/latest/)

## Bugs/Requests

Please use the [GitHub issue tracker](https://github.com/Metron-Project/mokkari/issues) to submit bugs or request features.

## License

This project is licensed under the [GPLv3 License](LICENSE).
