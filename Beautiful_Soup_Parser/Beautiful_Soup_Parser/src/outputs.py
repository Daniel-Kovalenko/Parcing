import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT


def control_output(results, cli_args):
    output = cli_args.output
    if output == 'file':
        OUTPUT_TYPES[output](results, cli_args)
    else:
        OUTPUT_TYPES[output](results)


def show_results(results, cli_args):
    output = cli_args.output
    OUTPUT_TYPES.get(output, default_output)(results, cli_args)


def default_output(results):
    for row in results:
        print(*row)


def pretty_output(results):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now().strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        csv.writer(f, dialect='unix').writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')


OUTPUT_TYPES = {
    'pretty': pretty_output,
    'file': file_output,
    None: default_output
}