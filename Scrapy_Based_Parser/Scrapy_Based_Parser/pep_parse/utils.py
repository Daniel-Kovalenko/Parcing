import csv


def dict_to_csv(filename, dict_data, head):
    file = [head]
    file.extend(dict_data.items())
    file.append(('Total', sum(dict_data.values())))
    with open(filename, mode='w', encoding='utf-8') as filename:
        writer = csv.writer(filename)
        writer.writerows(file)
