import sys
import os
import oss2
import re
from itertools import islice
import glob

if len(sys.argv) < 2:
    exit(1)
version = sys.argv[1]
chainfile = ''
chains = []

access_key_id = os.getenv('aliyun_access_key_id', '')
access_key_secret = os.getenv('aliyun_secret_access_key', '')
bucket_name = os.getenv('bucket_name', '')
endpoint = os.getenv('endpoint', '')

for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    if param == '':
        assert 'please set environment param'

if 0 < len(glob.glob('neo-cli/Chain*')):
    exit(0)

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

for b in islice(oss2.ObjectIterator(bucket), 100):
    if re.match('^' + version + '-*', b.key):
        print(b.key)
        chains.append(b.key)
chains.sort( None, None, True)

if 0 < len(chains):
    chainfile = chains[0]

if chainfile != '':
    destfile = 'neo-cli/' + chainfile
    print('download chain data: ' + chainfile)
    bucket.get_object_to_file( chainfile, destfile)
    result = os.system('unzip ' + destfile + ' -d ./neo-cli')
    os.remove(destfile)

        