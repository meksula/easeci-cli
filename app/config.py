protocol = 'http'
url = 'localhost'
port = '8080'

routes = {
    'state': {
        'method': 'GET',
        'uri': '/plugin/state'
    },
    'details': {
        'method': 'GET',
        'uri': '/plugin/details/{plugin_name}/{plugin_version}'
    }
}


def get_url(route_name, params):
    route = routes[route_name]
    uri = route['uri']
    method = route['method']
    complete_url = protocol + '://' + url + ':' + port + uri

    for key in params:
        complete_url = str.replace(complete_url, '{' + key + '}', params[key])

    return (method, complete_url)
