from colorama import Fore


def header(prompt_head):
    print(Fore.GREEN, '\033[1m' + prompt_head + '\033[0m', Fore.RESET, end='')


def bye():
    print(Fore.CYAN, '\n👋' + ' Bye! ' + '👋\n', Fore.RESET)


def err(communicate):
    print(Fore.RED, communicate, Fore.RESET)


def stdout(content):
    print(content)

