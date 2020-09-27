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
    separator = ''

    def deconstruct():
        all_rows = []
        for row in rows:
            if type(row) is not dict:
                row = row.__dict__
            row_deconstructed = []
            for k in row.keys():
                row_deconstructed.append(row.get(k))
            all_rows.append(row_deconstructed)
        return all_rows

    dec = deconstruct()
    dec.insert(0, columns)

    len_dict = {}
    for tab in dec:
        for index, item in enumerate(tab):
            if len_dict.get(index) is None:
                len_dict[index] = len(item)
            else:
                if len(item) > len_dict.get(index):
                    len_dict[index] = len(item)
    for tab in dec:
        for index, item in enumerate(tab):
            if len(tab[index]) < len_dict[index]:
                tab[index] = tab[index] + ' ' * (len_dict[index] - len(tab[index]))
    sep_parts = []
    for key in len_dict.keys():
        sep = '+' + ('-' * (len_dict.get(key) + 2))
        sep_parts.append(sep)
        separator = ' ' + ''.join(sep_parts) + '+'

    def assembly(row_as_list):
        row = ''
        for i, c in enumerate(row_as_list):
            row = row + ' | ' + row_as_list[i]
            if i + 1 == len(row_as_list):
                row = row + ' | '
        return row

    result_arr = []
    for arr in dec:
        result_arr.append(separator)
        result_arr.append(assembly(arr))
    result_arr.append(separator)

    header('📝' + title + '\n')
    print('\n'.join(result_arr)[1:], end='\n')

