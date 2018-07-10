import sys
import os
import oss2
import re
from itertools import islice
import glob

def isVersion(ver):
    return re.match(r'^(\d+\.){2}\d+$', ver)

def checkOldChain():
    chaindirs = glob.glob('neo-cli/Chain*')
    if 0 < len(chaindirs):
        print('[sync][checkOldChain] old chain data found, Scrubbing..')
        for dir in chaindirs:
            os.system('rm -rf ' + dir)
    print('[sync] Scrubbed.')

version = ''
chainfile = ''
chains = []
access_key_id = os.getenv('aliyun_access_key_id', '')
access_key_secret = os.getenv('aliyun_secret_access_key', '')
bucket_name = os.getenv('bucket_name', '')
endpoint = os.getenv('endpoint', '')

if len(sys.argv) < 2:
    print('[sync] no version')
    exit(1)

version = sys.argv[1]
if not isVersion(version):
    print('[sync] invalid version')
    exit(1)

for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    if param == '':
        assert '[sync] please set environment param'

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

checkOldChain()

for b in islice(oss2.ObjectIterator(bucket), 100):
    if re.match('^' + version + '-*', b.key):
        print(b.key)
        chains.append(b.key)

if 0 < len(chains):
    chains.sort( None, None, True)
    chainfile = chains[0]
else:
    print('[sync] no chan candidate.')
    exit(0)

destfile = 'neo-cli/' + chainfile
print('[sync] download chain data: ' + chainfile)
bucket.get_object_to_file( chainfile, destfile)
print('[sync] extracting...')
result = os.system('unzip ' + destfile + ' -d ./neo-cli')
os.remove(destfile)
print('[sync] done')

        