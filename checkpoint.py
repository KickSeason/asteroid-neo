#import boto3
import oss2
import os
import json
from itertools import islice

CHECKPOINT_DELTA = 25200 #blocks
HEIGHT = 0
CLI_VERSION = '0'

with open('state.json', 'rb') as stateFile:
    res = json.load(stateFile)
    HEIGHT = res['height']
    CLI_VERSION = res['version']



def getMaxCheckpoint():
    maxHeight = 0
    for obj in islice(oss2.ObjectIterator(bucket), 100):
        destruct = obj.key.split('-')
        destruct[2] = int(destruct[2].split('.')[0])
        if (destruct[0] == CLI_VERSION) and (destruct[2] > maxHeight):        
            maxHeight = destruct[2]

    return maxHeight


def uploadCheckpoint():
    filename = '{0}-mainnet-{1}.zip'.format(CLI_VERSION, str(HEIGHT))
    print 'zippy zippy'
    os.system('zip -r {0} neo-cli/Chain_*'.format(filename))
    # data = open(filename, 'rb')
    print 'uploading'
    # bucket.put_object(Key=filename, Body=data, ACL='public-read')
    bucket.put_object_from_file(filename, filename)
    # data.close()
    os.remove(filename)
    print 'done'





# s3 = boto3.resource('s3')
# bucket = s3.Bucket('chainneo')

access_key_id = os.getenv('aliyun_access_key_id', '')
access_key_secret = os.getenv('aliyun_secret_access_key', '')
bucket_name = os.getenv('bucket_name', '')
endpoint = os.getenv('endpoint', '')

for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    if param == '':
        assert 'please set environment param'

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

mCheckpoint = getMaxCheckpoint()
print 'max: {}'.format(mCheckpoint)
print 'height: {}'.format(HEIGHT)
print 'aliyun-height: {}'.format(mCheckpoint)
 
if HEIGHT - mCheckpoint >= CHECKPOINT_DELTA:
    print 'time to upload'
    print HEIGHT
    print mCheckpoint
    uploadCheckpoint()



