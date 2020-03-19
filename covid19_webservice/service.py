#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__license__ = "The MIT License (MIT)"


from gevent.pywsgi import WSGIServer
from covid19_webservice.webservice.flask_webservice import service


def print_message(message):
    print('\n\n%s\n\n' % message)


def run(ip, port):
    http_server = WSGIServer((ip, port), service)
    print_message('Serving %s on http://%s:%s' % (service.name, ip, port))
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print_message('Shutting down %s ...' % service.name)


