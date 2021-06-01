import struct
from pprint import pformat

from django.utils.http import parse_qsl


def application(environ, start_response):
    output = [str.encode(environ['REQUEST_METHOD']) + b'\n']

    d = parse_qsl(environ['QUERY_STRING'])
    if environ['REQUEST_METHOD'] == 'POST':
        output.append(str.encode('Post data:\n'))
        output.append(str.encode(pformat(environ['wsgi.input'].read())))

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            output.append(str.encode('Get data:\n'))
            for ch in d:
                output.append(str.encode(' = '.join(ch)))
                output.append(str.encode('\n'))

    start_response('200 OK', [('Content-type', 'text/plain')])
    return output
