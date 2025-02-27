def calculate_suitability_index(scouting_data, statbotics_data):
    # Calculate the suitability index for each team based on the scouting data.
    suitability_indices = {}

    for team, metrics in scouting_data.items():
        # Calculate the suitability index for the team
        suitability_indices[team] = sum(metrics) / len(metrics)

    for team, metrics in statbotics_data.items():
        # Calculate the suitability index for the team
        suitability_indices[team] += metrics['epa_end']

    return suitability_indices
