#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__license__ = "The MIT License (MIT)"

from covid19_webservice import service
import os

ip = '0.0.0.0'
port = int(os.environ['PORT'])

if __name__ == '__main__':
    service.run(ip, port)
