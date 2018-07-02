#can get this info from neo-cli...
version="2.7.6"

service cron start


cd /var/www/asteroid-neo


if [ -d "neo-cli/Chain" ] && [ ! -f "neo-cli/Chain/$version" ] ; then
    echo "Old Chain Found...Scrubbing"
    rm -rf neo-cli/Chain/*
fi


# if [ ! "$(ls -A neo-cli/Chain)" ] ; then
#     chain=$(aws s3 ls s3://chainneo --no-sign-request | awk '{print $4}' | sort -r | grep -m 1 $version)
#     echo "Downloading: $chain"

#     wget "https://s3.amazonaws.com/chainneo/$chain"    
 
#     echo "Extracting: $chain"
#     unzip "$chain"
#     #mv Chain/* neo-cli/Chain
#     touch "neo-cli/Chain/$version"

#     rm "$chain"
#     rm -rf Chain

# fi

python sync.py $version

if [ -z ${aliyun_access_key_id+x} ] || [ -z ${aliyun_secret_access_key+x} ]; then
    echo "running in slave mode"
    expect ./neo.sh 0
else      
    echo "[default]" >> ~/.aliyun/credentials
    echo "aliyun_access_key_id = $aliyun_access_key_id" >> ~/.aliyun/credentials
    echo "aliyun_secret_access_key = $aliyun_secret_access_key" >> ~/.aliyun/credentials
    echo "bucket_name = $bucket_name" >> ~/.aliyun/credentials
    echo "endpoint = $endpoint" >> ~/.aliyun/credentials
    while :
    do
        echo "Running in master mode | Hopefully your credentials are good..."
        expect ./neo.sh 1
        echo "checkpoint"
        python checkpoint.py
    done    
fi
