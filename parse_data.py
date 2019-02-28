import csv


def find_first_V(data_set):
    current_V = None

    for row in data_set:
        if row[1] == 'V':
            current_V = row
            del data_set[data_set.index(row)]
            break

    return current_V


def process_data(data_set):
    current_V = find_first_V(data_set)

    while current_V != None:
        for row in data_set:
            if row[1] == 'V':
                data_set.append(((current_V[0], row[0]), 'W',
                                 list(set(current_V[2] + row[2]))))

        current_V = find_first_V(data_set)


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

    process_data(data_set)

    return data_set