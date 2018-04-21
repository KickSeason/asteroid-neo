import boto3
import os
import json

CHECKPOINT_DELTA = 25200 #blocks
HEIGHT = 0
CLI_VERSION = '0'

with open('state.json', 'rb') as stateFile:
    res = json.load(stateFile)
    HEIGHT = res['height']
    CLI_VERSION = res['version']



def getMaxCheckpoint():
    maxHeight = 0
    for obj in bucket.objects.all():
        destruct = obj.key.split('-')
        destruct[2] = int(destruct[2].split('.')[0])
        if (destruct[0] == CLI_VERSION) and (destruct[2] > maxHeight):        
            maxHeight = destruct[2]

    return maxHeight


def uploadCheckpoint():
    filename = '{0}-mainnet-{1}.zip'.format(CLI_VERSION, str(HEIGHT))
    print 'zippy zippy'
    os.system('zip -r {0} neo-cli/Chain'.format(filename))
    data = open(filename, 'rb')
    print 'uploading'
    bucket.put_object(Key=filename, Body=data, ACL='public-read')
    data.close()
    os.remove(filename)
    print 'done'





s3 = boto3.resource('s3')
bucket = s3.Bucket('chainneo')

mCheckpoint = getMaxCheckpoint()
print 'max: {}'.format(mCheckpoint)
print 'height: {}'.format(HEIGHT)


 
if HEIGHT - mCheckpoint >= CHECKPOINT_DELTA:
    print 'time to upload'
    print HEIGHT
    print mCheckpoint
    uploadCheckpoint()



