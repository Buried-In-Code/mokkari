"""Test Cache module.

This module contains tests for SqliteCache objects.
"""

from __future__ import annotations

import pytest
import requests_mock

from mokkari import api, exceptions


class NoGet:
    """The NoGet object fakes storing data from the sqlite cache."""

    def store(self: NoGet, key: any, value: any) -> None:  # noqa: ARG002
        """Save no data."""
        # This method should store key value pair
        return


class NoStore:
    """The NoStore object fakes getting data from the sqlite cache."""

    def get(self: NoStore, key: any) -> None:  # noqa: ARG002
        """Retrieve no data."""
        return


def test_no_get(dummy_username: str, dummy_password: str) -> None:
    """Test for retrieving failure."""
    m = api(username=dummy_username, passwd=dummy_password, cache=NoGet())

    with pytest.raises(exceptions.CacheError):
        m.series(5)


def test_no_store(dummy_username: str, dummy_password: str) -> None:
    """Test for saving data error."""
    m = api(username=dummy_username, passwd=dummy_password, cache=NoStore())

    with requests_mock.Mocker() as r:
        r.get("https://metron.cloud/api/series/5/", text='{"response_code": 200}')

        with pytest.raises(exceptions.CacheError):
            m.series(5)
