import statbotics

import constants

sb = statbotics.Statbotics()


def get_statbotics_stats_from_scouting_data(data):
    sb_data = {}
    for team, metrics in data.items():
        sb_data[team] = sb.get_team_year(team, constants.YEAR)
    return sb_data
