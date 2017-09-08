from requests import post
import argparse
parser = argparse.ArgumentParser(description='POST utility')
parser.add_argument('--file', '-f', action='store', required=True)
parser.add_argument('--address', '-a', action='store', required=True)
clargs = parser.parse_args()

MSG = 'Sending {} to {}...'.format(clargs.file, clargs.address)
#print(MSG)
try:
    r = post(clargs.address, files={'file': (clargs.file, open(clargs.file, 'rb'))})
    print(r.text)
except:
    raise
