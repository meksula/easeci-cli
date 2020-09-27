import json
import socket
import sys

from app.command import Cmd
from app.output import bye, err, stdout, table
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
        def __init__(self, response, host):
            self.host = host
            self.node_name = response.get('nodeName')
            self.connection_uuid = response.get('connectionUuid')
            self.username = response.get('username')
            self.connection_state = response.get('connectionState')

    class ConnectionList:
        class Connection:
            def __init__(self, conn):
                self.connection_uuid = conn.get('connectionUuid')
                self.connection_state = conn.get('connectionState')
                self.username = conn.get('username')
                self.host = conn.get('host')

            def __str__(self):
                return f"Connection(connection_uuid={self.connection_uuid}, " \
                       f"connection_state={self.connection_state}," \
                       f" username={self.username}, host={self.host})"

        def __init__(self, response):
            self.connections = [self.Connection(conn) for conn in response]

    def invoke(self, ctx, params):
        option = params[self._option]
        if option == 'connect':
            if ctx.connected:
                err(f' You are now connected to EaseCI Core server.\n   Close connection and next establish new one.')
                return
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
                    conn_resp = self.ConnectionResponse(resp_json, host)
                    if conn_resp.connection_state == 'ESTABLISHED':
                        stdout(f' 🔌 Now you are connected to {host} as {username}')
                        ctx.connect(conn_resp)
                        return
                    elif conn_resp.connection_state == 'CONNECTIONS_LIMIT':
                        stdout(f' You received limit of connections as {username}')
                    else:
                        err(f' Some unrecognized error occurred while connection attempt to {host}')
                else:
                    err(f' Server responded with HTTP code: {resp.status}, could not established connection')
            except socket.gaierror:
                err(f' Host {host} is not recognizable')
            except ConnectionRefusedError:
                err(f' Host {host} is not reachable')
        if option == 'disconnect':
            if not ctx.connected:
                err(f' Connection is not established')
                return
            else:
                stdout(f' Closing your connection identified by UUID: {ctx.connection_uuid}')
                ctx.disconnect()
        if option == 'connection':
            standalone_params = params.get('standalone')
            if '-l' in standalone_params or '--list' in standalone_params:
                additional_cmd = 'list'
            else:
                return
            if additional_cmd == 'list':
                if ctx.connected:
                    connection = http.client.HTTPConnection(ctx.host)
                    connection.request('GET', '/client/connections')
                    resp = connection.getresponse()
                    resp_json = json.loads(resp.read().decode())
                    conn_list = self.ConnectionList(resp_json)

                    _columns = [
                        'Connection UUID',
                        'Connection State',
                        'Username',
                        'Connected IP'
                    ]
                    table(_columns,
                          conn_list.connections,
                          title='List of connections of ' + ctx.host + ' node')
                else:
                    err(' First of you need to connect some EaseCI Core server')
