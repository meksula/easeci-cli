from colorama import Fore


def header(prompt_head):
    print(Fore.GREEN, '\033[1m' + prompt_head + '\033[0m', Fore.RESET, end='')


def bye():
    print(Fore.CYAN, '\n👋' + ' Bye! ' + '👋\n', Fore.RESET)


def err(communicate):
    print(Fore.RED, communicate, Fore.RESET)


def stdout(content):
    print(content)


def table(columns, rows, title=''):
    _separator = ' +--+--+--+--+--+'
    # print(f'| {columns[0]} | | | | |')
    # print('+--+--+--+--+--+')
    # print('| | | | | |')
    # print('+--+--+--+--+--+')
    # print('| | | | | |')
    # print('+--+--+--+--+--+')
    # print('| | | | | |')
    rows_to_print = []
    # print(' +--+--+--+--+--+')
    # def generate_header_row():
    #     row = ''
    #     for i, c in enumerate(columns):
    #         row = row + ' | ' + c
    #         if i + 1 == len(columns):
    #             row = row + ' | '
    #         rows_to_print.append(row)

    def generate_head_row(data_row):
        row = ''
        for i, c in enumerate(data_row):
            row = row + ' | ' + c
            if i + 1 == len(data_row):
                row = row + ' | '
        return row

    def generate_data_row(data_row):
        row = ''
        for i, c in enumerate(data_row):
            data_row.get(c)
            row = row + ' | ' + data_row.get(c)
            if i + 1 == len(data_row):
                row = row + ' | '
        return row

    def iterate_data():
        for data_row in rows:
            rows_to_print.append(_separator)
            generated = generate_data_row(data_row)
            rows_to_print.append(generated)

    rows_to_print.append(_separator)
    rows_to_print.append(generate_head_row(columns))
    iterate_data()
    rows_to_print.append(_separator)

    def find_longest_index():
        longest_index = 0
        max_length = 0
        for i, r in enumerate(rows_to_print):
            if i % 2 > 0:
                if len(r) > max_length:
                    max_length = len(r)
                    longest_index = i
        return longest_index

    def align(row, longest_row):
        row = ' '
        splitted = longest_row.split('|')
        for part in splitted[1:-1]:
            part_l = len(part)
            row = row + '+'
            for _ in range(part_l):
                row = row + '-'
        return row + '+'

    longest = rows_to_print[find_longest_index()]
    separator_aligned = align(rows_to_print[0], longest)

    for i, item in enumerate(rows_to_print):
        if item == _separator:
            rows_to_print[i] = separator_aligned

    print('\n'.join(rows_to_print))
