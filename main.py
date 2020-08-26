from app.config import get_url
from app.runtime import Context
from colorama import init, Fore

if __name__ == '__main__':
    init()
    url = get_url('details', {'plugin_name': 'time-printer', 'plugin_version': '0.0.1'})
    print(Fore.CYAN, ' ')
    print('   _____                    _    ____ _     ___ ')
    print('  | ____|__ _ ___  ___  ___(_)  / ___| |   |_ _|')
    print('  |  _| / _` / __|/ _ \/ __| | | |   | |    | | ')
    print('  | |__| (_| \__ \  __/ (__| | | |___| |___ | | ')
    print('  |_____\__,_|___/\___|\___|_|  \____|_____|___|')
    print('')
    print(' ~ developed by Karol Meksuła 2020  🚀', Fore.RESET)
    print('')

    ctx = Context()
    ctx.event_loop()
