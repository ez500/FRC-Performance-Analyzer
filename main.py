import scouting_data_import as sdi
import statbotics_data_import as sbdi
import suitability_index_integration as sii


def main():
    scouted_data = sdi.populate_scouted_data()
    statbotics_data = sbdi.get_statbotics_stats_from_scouting_data(scouted_data)
    suitability_indices = sii.calculate_suitability_index(scouted_data, statbotics_data)

    # TODO CREATE A RELIABILITY FACTOR FOR SCOUTED DATA DEPENDING ON CONSISTENCY OF CONTRIBUTION TO A MATCH SCORE I.E., IF A MATCH SCORE IS HIGHER THAN EPA EXPECTED, THEN SCOUTED DATA IS RELIABLE IF TEAM SCORED HIGHER THAN PROPORTIONAL EPA
    # TODO TEST FRC API 2023 DATA

    for team, index in suitability_indices.items():
        print(f'{team}: {index}')


if __name__ == '__main__':
    main()
