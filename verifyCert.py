#!/usr/bin/env python3
import datetime
import calendar
import time
from urllib.request import ssl, socket
hostname = 'www.jonaslarson.se'
port = '443'
context = ssl.create_default_context()
d = dict((v, k) for k, v in enumerate(calendar.month_abbr))
int_month = 0

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        certificate = ssock.getpeercert()

st = certificate['notAfter'].split()

for k in d.keys():
    if st[0] in k:
        int_month = d[k]

cert_expiration = int(datetime.datetime(int(st[3]), int_month, int(st[1]), 0, 0).timestamp())
seconds_until_expired = cert_expiration - int(time.time())

print("""
    {} seconds until cert expires
    {} days
    {} weeks
""".format(seconds_until_expired, int(seconds_until_expired / (24 * 3600)),
           int(seconds_until_expired / (24 * 3600 * 7))))
