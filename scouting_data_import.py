import csv


def check_validity(row) -> bool:
    return row[0] == 'Team' and row[1] == 'Coral'

# TODO JSON READER INSTEAD OF CSV, WITH STRUCTURE SENT BY GERSE
def populate_scouted_data():
    data = {}
    with open('data.csv', newline='') as file:
        reader = csv.reader(file)
        if not check_validity(next(reader)):
            print('Invalid data')
            return
        for team in reader:
            metric_cycle = iter(team)
            data[int(next(metric_cycle))] = []
            for metric in metric_cycle:
                data[int(team[0])].append(int(metric))
    return data
