import itertools

from marshmallow import ValidationError

from mokkari import exceptions, team


class TeamsList:
    def __init__(self, response):
        self.teams = []
        self.response = response

        schema = team.TeamSchema()
        for team_dict in response["results"]:
            try:
                result = schema.load(team_dict)
            except ValidationError as error:
                raise exceptions.ApiError(error)

            self.teams.append(result)

    def __iter__(self):
        return iter(self.teams)

    def __len__(self):
        return len(self.teams)

    def __getitem__(self, index):
        try:
            return next(itertools.islice(self.teams, index, index + 1))
        except TypeError:
            return list(
                itertools.islice(self.teams, index.start, index.stop, index.step)
            )