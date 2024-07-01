=======
Mokkari
=======

.. |Python| image:: https://img.shields.io/badge/Python-3%2E8%20%7C%203%2E9-green?logo=Python&style=flat-square
   :alt: Python
.. |Status| image:: https://img.shields.io/pypi/status/mokkari.svg?logo=Python&label=Status&style=flat-square
   :target: https://pypi.org/project/mokkari
   :alt: Status
.. |Version| image:: https://img.shields.io/pypi/v/mokkari.svg?logo=Python&label=Version&style=flat-square
   :target: https://pypi.org/project/mokkari
   :alt: Version
.. |License| image:: https://img.shields.io/github/license/bpepple/mokkari?logo=Python&label=License&style=flat-square
   :target: https://opensource.org/licenses/GPL-3.0
   :alt: License

.. |Hatch| image:: https://img.shields.io/badge/Packaging-Hatch-4051b5?style=flat-square
   :target: https://github.com/pypa/hatch
   :alt: Hatch
.. |Pre-Commit| image:: https://img.shields.io/badge/Pre--Commit-Enabled-informational?style=flat-square&logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit
   :alt: Pre-Commit
.. |Linter| image:: https://img.shields.io/badge/Linter-Ruff-informational?style=flat-square
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff (Linter)
.. |Formatter| image:: https://img.shields.io/badge/Formatter-Ruff-informational?style=flat-square
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff (Formatter)

.. |Tests| image:: https://img.shields.io/github/actions/workflow/status/Buried-In-Code/mokkari/testing%2Eyaml?branch=main&logo=Github-Actions&label=Tests&style=flat-square
   :target: https://github.com/Buried-In-Code/mokkari/actions/workflows/testing%2Eyaml

|Python| |Status| |Version| |License|

|Hatch| |Pre-commit| |Linter| |Formatter|

|Tests|

Quick Description
-----------------

A backport for Python 3.8 & Python 3.9 of the python wrapper for the metron.cloud_ API.

.. _metron.cloud: https://metron.cloud

Installation
------------

Add the following to your pyproject:

.. code-block:: toml

  dependencies = [
    "mokkari@git+https://github.com/Buried-In-Code/mokkari ; python_version < \"3.10\""
  ]

Example Usage
-------------

.. code-block:: python

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

Documentation
-------------

- `Read the project documentation <https://mokkari.readthedocs.io/en/latest/>`_

Bugs/Requests
-------------

Please use the `GitHub issue tracker <https://github.com/Metron-Project/mokkari/issues>`_ to submit bugs or request features.

License
-------

This project is licensed under the `GPLv3 License <LICENSE>`_.
