import csv


def check_validity(row) -> bool:
    return row[0] == 'Team' and row[1] == 'Coral'


def populate_scouted_data(data):
    with open('data.csv', newline='') as file:
        reader = csv.reader(file)
        if not check_validity(next(reader)):
            print('Invalid data')
            return
        for team in reader:
            metric_cycle = iter(team)
            data[next(metric_cycle)] = []
            for metric in metric_cycle:
                data[team[0]].append(int(metric))


def get_scouted_dict():
    scouted_data = {}
    populate_scouted_data(scouted_data)
    return scouted_data
