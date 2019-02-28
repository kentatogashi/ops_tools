#!/usr/bin/env python
import re
import sys
import json
import requests
import argparse
import warnings

warnings.filterwarnings('ignore')

HOST = '192.168.0.3'
LOGINCHECK_API = 'https://{host}/logincheck'.format(host=HOST)
ADDRESS_API = 'https://{host}/api/v2/cmdb/firewall/address'.format(host=HOST)
FILE = './addresses.txt'


def get_cookies(user, password):
    payload = {'username': user, 'secretkey': password}
    r_login = requests.post(LOGINCHECK_API, data=payload, verify=False)
    if r_login.status_code != 200:
        sys.stderr.write('failed to login')
        sys.exit(1)
    return r_login.cookies


def get_addrs(cookies):
    r_address = requests.get(ADDRESS_API, cookies=cookies, verify=False)
    if r_address.status_code != 200:
        sys.stderr.write('failed to get addresses.')
        sys.exit(1)
    return json.loads(r_address.text)['results']


def save_addrs(results):
    regex_ip = r'(IP_)?([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
    with open(FILE, 'w') as f:
        for result in results:
            m = re.match(regex_ip, result['name'])
            if m:
                f.write(m.group(2) + "\n")


def main():
    parser = argparse.ArgumentParser(description='Get firewall policy.')
    parser.add_argument('--user', help='fortigate login user', required=True)
    parser.add_argument('--password', help='fortigate login password', required=True)
    args = parser.parse_args()
    cookies = get_cookies(args.user, args.password)
    results = get_addrs(cookies)
    save_addrs(results)


if __name__ == '__main__':
    main()
