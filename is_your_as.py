import subprocess
import re
import sys

"""
$ python is_your_as_ipaddr.py 192.168.0.1 xxxx
192.168.0.1 is in ASxxxx.
"""

def is_your_ip_addr(ipddr, as_):
    irr = 'jpirr.nic.ad.jp'
    cmd = 'whois -h %s %s' % (irr, ipaddr)
    try:
        res = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        raise e

    for line in res.decode().split('\n'):
        if re.match(r'^origin:.*AS%s$' % as_, line):
            return True

    return False

if __name__ == '__main__':
    _, ipaddr, as_ = sys.argv
    if is_your_ip_addr(ipaddr, as_):
        print('%s is your ipaddr' % ipaddr)
    else:
        print('%s is not your ipaddr' % ipaddr)
