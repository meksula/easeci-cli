import sys
from app.output import bye, header, err
from app.set.cmds_dict import cmds_av


class Context:

    def __init__(self):
        self.is_interrupted = False
        self.cmd_hist = []
        self.cmd_curr = ''
        self.connected = False
        self.whoami = 'not-connected@local'
        self.prompt_head = self.whoami + ':~$'

    def event_loop(self):
        while not self.is_interrupted:
            self.prompt()
            self.exec()

    def prompt(self):
        try:
            header(self.prompt_head)
            self.cmd_curr = input()
            self.cmd_hist.append(self.cmd_curr)
        except KeyboardInterrupt:
            bye()
            sys.exit()

    def exec(self):
        if self.cmd_curr == '':
            return
        cmd_name = self.extract_cmd_name(self.cmd_curr)
        cmd_name = cmd_name.strip(" ")
        cmd = cmds_av.get(cmd_name)
        if cmd is None:
            err('⛔ Command named \'' + cmd_name + '\' not exists! Type \'cmd list\' to list all available commands.')
        else:
            cmd.handle(self.cmd_curr)

    def extract_cmd_name(self, cmd):
        parts = cmd.split()
        if len(parts) >= 1:
            return parts[0]
        else:
            return ''
