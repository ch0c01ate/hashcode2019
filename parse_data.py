import csv


def parse(file_name):
    data_set = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=' ')
        identifier = 0
        for row in reader:
            if len(row) < 3:
                continue

            data_set.append((identifier, row[0], row[2:]))
            identifier += 1

    return data_set