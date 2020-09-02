import json
import unittest

from app.output import table


class TestOutput(unittest.TestCase):

    def test_print_table(self):
        _json_data = '[{"connectionUuid":"4899c481-6977-4509-9bab-4ccc71be5bfa","connectionState":"ALIVE","username":"meksula","host":"127.0.0.1"},' \
                     '{"connectionUuid":"8c426ad2-48c3-4f23-b027-61c30a32021a","connectionState":"ALIVE","username":"jyoung","host":"127.0.0.1"},' \
                     '{"connectionUuid":"d725b5ba-089c-4f6a-a649-8e4ea96b047c","connectionState":"ALIVE","username":"neilsbohr","host":"127.0.0.1"},' \
                     '{"connectionUuid":"5e3009f8-35a9-4e45-a4b8-c3d5fe0e312d","connectionState":"ALIVE","username":"gandhi","host":"127.0.0.1"},' \
                     '{"connectionUuid":"50227e3c-f920-415f-b903-7b08ba50e6b9","connectionState":"ALIVE","username":"johndoe","host":"127.0.0.1"},' \
                     '{"connectionUuid":"ef795185-fe4e-475f-bc90-d293bd9a330d","connectionState":"ALIVE","username":"ansible","host":"127.0.0.1"},' \
                     '{"connectionUuid":"84e962e3-40e5-46e4-8bfc-7151efd89689","connectionState":"ALIVE","username":"admin","host":"127.0.0.1"}]'
        _column_names = [
            'Connection UUID',
            'Connection State',
            'Username',
            'Connected IP'
        ]

        table(
            _column_names,
            json.loads(_json_data),
            title='Established connections with EaseCI Core server'
        )