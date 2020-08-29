import json
import socket
import sys

from app.command import Cmd
from app.output import bye, err, stdout
import http.client


# This command simply ends program
class Exit(Cmd):
    def invoke(self, ctx, params):
        bye()
        sys.exit()


# This command tries to connect with EaseCI core in specified address, credentials etc.
class Connect(Cmd):
    class ConnectionRequest:
        def __init__(self, username):
            self.username = username

    class ConnectionResponse:
        def __init__(self, response):
            self.node_name = response.get('nodeName')
            self.connection_uuid = response.get('connectionUuid')
            self.username = response.get('username')
            self.connection_state = response.get('connectionState')

    def invoke(self, ctx, params):
        option = params[self._option]
        if option == 'connect':
            host = ''
            username = ''
            protocol = None
            if params.get('-h') is not None:
                host = params.get('-h')
            if params.get('--host') is not None:
                host = params.get('--host')
            if params.get('-u') is not None:
                username = params.get('-u')
            if params.get('--username') is not None:
                username = params.get('--username')
            if params.get('--protocol') is not None:
                protocol = params.get('--protocol')
            if len(host) == 0:
                err('Host not specified in command.')
                return
            if len(username) == 0:
                err('Username not specified in command.')
                return
            connection = None
            if protocol is None or protocol == 'HTTP':
                protocol = 'HTTP'
                connection = http.client.HTTPConnection(host)
            elif protocol == 'HTTPS':
                connection = http.client.HTTPSConnection(host)
            else:
                err(f' Protocol {protocol} is not available')
                return
            req = self.ConnectionRequest(username)
            body = json.dumps(req.__dict__)

            try:
                connection.request('POST', '/client/connection/open', body)
                resp = connection.getresponse()
                if resp.status == 200:
                    resp_json = json.loads(resp.read().decode())
                    conn_resp = self.ConnectionResponse(resp_json)
                    ctx.connect(conn_resp)
                    if conn_resp.connection_state == 'ESTABLISHED':
                        stdout(f' 🔌 Now you are connected to {host} as {username}')
                    if conn_resp.connection_state == 'CONNECTIONS_LIMIT':
                        stdout(f' You received limit of connections as {username}')
                    else:
                        err(f' Some unrecognized error occurred while connection attempt to {host}')
                else:
                    err(f' Server responded with HTTP code: {resp.status}, could not established connection')
            except socket.gaierror:
                err(f' Host {host} is not recognizable')
            except ConnectionRefusedError:
                err(f' Host {host} is not reachable')

