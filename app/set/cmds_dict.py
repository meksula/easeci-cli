from app.command import Cmd
from app.output import err
from app.set.builtin_cmds import Exit, Connect

cmds_av = {
    'exit': Exit('exit', '', '', []),
    'cmd': Cmd('cmd', 'Error cmd command', 'Info about cmd command', ['list']),
    'ease': Connect('ease', 'Error', 'Info', ['connect', 'ping'])
}


def add_cmd(cmd):
    if cmd.name in cmds_av.keys:
        err('⛔ Cannot add command, because one with this $cmd.name name exists!')
    else:
        cmds_av[cmd.name] = cmd


def cmds_list():
    for cmd in cmds_av:
        print(cmd, end='\n')
