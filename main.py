import scouting_data_import as sdi
import suitability_index_integration as sii


def main():
    scouted_data = sdi.get_scouted_dict()
    suitability_indices = sii.calculate_suitability_index(scouted_data)

    for team, index in suitability_indices.items():
        print(f'{team}: {index}')


if __name__ == '__main__':
    main()
