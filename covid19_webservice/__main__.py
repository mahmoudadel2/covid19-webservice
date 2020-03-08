#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__license__ = "The MIT License (MIT)"

from covid19_webservice import service


ip = '127.0.0.1'
port = 8080

if __name__ == '__main__':
    service.run(ip, port)
