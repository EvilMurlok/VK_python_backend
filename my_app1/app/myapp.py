import json
from datetime import datetime


def app(environ, start_response):
    print(environ)
    data = json.dumps({
        'time': str(datetime.now()),
        'url': f"{environ['wsgi.url_scheme']}://{environ['REMOTE_ADDR']}:"
               f"{environ['SERVER_PORT']}{environ['PATH_INFO']}"
               f"{'?' + environ['QUERY_STRING'] if environ['QUERY_STRING'] else ''}"
    }).encode('utf-8')
    start_response('200 OK',
                   [('Content-Type', 'application/json'),
                    ('Content-Length', str(len(data)))])
    return iter([data])
