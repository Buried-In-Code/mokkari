import platform

import requests
from marshmallow import ValidationError
from ratelimit import limits, sleep_and_retry

from mokkari import (
    character,
    character_list,
    creator,
    creators_list,
    exceptions,
    publisher,
    publishers_list,
)

ONE_MINUTE = 60


class Session:
    def __init__(self, username, passwd) -> None:
        self.username = username
        self.passwd = passwd
        self.header = {
            "User-Agent": f"Mokkari/0.0.1 ({platform.system()}; {platform.release()})"
        }

    @sleep_and_retry
    @limits(calls=20, period=ONE_MINUTE)
    def call(self, endpoint, params=None):
        if params is None:
            params = {}

        api_url = "https://metron.cloud/api/{}/"
        url = api_url.format("/".join(str(e) for e in endpoint))
        response = requests.get(
            url, params=params, auth=(self.username, self.passwd), headers=self.header
        )
        return response.json()

    def creator(self, _id):
        try:
            result = creator.CreatorSchema().load(self.call(["creator", _id]))
        except ValidationError as error:
            raise exceptions.ApiError(error)

        result.session = self
        return result

    def creators_list(self, params=None):
        if params is None:
            params = {}
        return creators_list.CreatorsList(self.call(["creator"], params=params))

    def character(self, _id):
        try:
            result = character.CharacterSchema().load(self.call(["character", _id]))
        except ValidationError as error:
            raise exceptions.ApiError(error)

        result.session = self
        return result

    def characters_list(self, params=None):
        if params is None:
            params = {}
        return character_list.CharactersList(self.call(["character"], params=params))

    def publisher(self, _id):
        try:
            result = publisher.PublisherSchema().load(self.call(["publisher", _id]))
        except ValidationError as error:
            raise exceptions.ApiError(error)

        result.session = self
        return result

    def publishers_list(self, params=None):
        if params is None:
            params = {}
        return publishers_list.PublishersList(self.call(["publisher"], params=params))
