import datetime

import pytest
from mokkari import exceptions, issues_list


def test_known_issue(talker):
    death = talker.issue(1)
    assert death.publisher.name == "Marvel"
    assert death.series.name == "Death of the Inhumans"
    assert death.volume == 1
    assert death.name[0] == "Chapter One: Vox"
    assert death.cover_date == datetime.date(2018, 9, 1)
    assert death.store_date == datetime.date(2018, 7, 4)
    assert (
        death.image
        == "https://static.metron.cloud/media/issue/2018/11/11/6497376-01.jpg"
    )
    assert len(death.characters) > 0
    assert len(death.teams) > 0
    assert len(death.credits) > 0


def test_issue_without_store_date(talker):
    spidey = talker.issue(31047)
    assert spidey.publisher.name == "Marvel"
    assert spidey.series.name == "The Spectacular Spider-Man"
    assert spidey.volume == 1
    assert spidey.name[0] == "A Night on the Prowl!"
    assert spidey.cover_date == datetime.date(1980, 10, 1)
    assert spidey.store_date is None
    assert "Dennis O'Neil" in [c.creator for c in spidey.credits]
    assert "Spider-Man" in [c.name for c in spidey.characters]


def test_issueslist(talker):
    issues = talker.issues_list()
    assert len(issues.issues) > 0


def test_bad_issue(talker):
    with pytest.raises(exceptions.ApiError):
        talker.issue(-1)


def test_bad_response_data():
    with pytest.raises(exceptions.ApiError):
        issues_list.IssuesList({"results": {"volume": "1"}})
