# Mokkari

[![PyPI - Version](https://img.shields.io/pypi/v/mokkari.svg)](https://pypi.org/project/mokkari/)
![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9-informational)

[![Rye](https://img.shields.io/badge/Rye-informational?logo=rye&labelColor=grey)](https://rye.astral.sh)
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-informational?logo=pre-commit&labelColor=grey)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/badge/Ruff-informational?logo=ruff&labelColor=grey)](https://github.com/astral-sh/ruff)

A backport for Python 3.8 & 3.9 of the python wrapper for the [Metron Comic Book Database](https://metron.cloud) API.

## Installation

```toml
dependencies = [
    "mokkari@git+https://github.com/Buried-In-Code/mokkari ; python_version < \"3.10\""
]
```

## Example Usage

```python
import mokkari

# Your own config file to keep your credentials secret
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

[Read the project documentation](https://mokkari.readthedocs.io/en/stable/?badge=latest)

## Bugs/Requests

Please use the [GitHub issue tracker](https://github.com/Metron-Project/mokkari/issues) to submit bugs or request features.
