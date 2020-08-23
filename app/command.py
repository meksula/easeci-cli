from app.output import err, stdout


class Cmd:

    def __init__(self, cmd_name, err_txt, info, opts):
        self.name = cmd_name
        self.err_txt = err_txt
        self.short_info = info
        self.options = opts

    def info(self):
        stdout(self.short_info)

    def handle(self, keyboard_input):
        parsed = self.parse(keyboard_input)
        self.invoke(parsed)

    def parse(self, keyboard_input):
        parts = keyboard_input.split()
        params_dict = {'standalone': []}
        if len(parts) < 2:
            self.info()
            return params_dict
        option = parts[1]
        params_dict['cmd_opt'] = option
        if option not in self.options:
            err('⛔ Option named \'' + option + '\' not exists for \'' + parts[0] + '\' command! Type \'' + parts[0]
                + ' help\' to list all available options.')
            return params_dict

        def split_input():
            if '"' not in keyboard_input:
                return keyboard_input[len(parts[0]) + len(parts[1]) + 1:].split()
            else:
                to_split = keyboard_input[len(parts[0]) + len(parts[1]) + 1:] + ' '
                buffer = []
                params_resolved = []
                quoted_mode = False
                for char in to_split:
                    if char == '"':
                        quoted_mode = not quoted_mode
                        if not quoted_mode:
                            buffer.append('"')
                            params_resolved.append(''.join(buffer).strip())
                            buffer = []
                    if quoted_mode:
                        buffer.append(char)
                    if not quoted_mode:
                        if char == ' ':
                            collected = ''.join(buffer).strip()
                            buffer = []
                            if len(collected) > 1:
                                params_resolved.append(collected)
                        buffer.append(char)
                return params_resolved
        params = split_input()
        for index, param in enumerate(params, start=0):
            if param[0] == '-':
                if index + 1 < len(params) and params[index + 1][0] == '-':
                    params_dict['standalone'].append(params[index])
                elif index + 1 < len(params):
                    params_dict[params[index]] = params[index + 1]
                else:
                    params_dict['standalone'].append(params[index])
        return params_dict

    def invoke(self, params):
        raise NotImplementedError()

    # Should provide complete instance of specific child object
    # This should be work similar to builder pattern, but return default instance
    def build(self):
        pass
