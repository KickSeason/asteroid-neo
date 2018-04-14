
version="2.7.4"

cd /var/www/asteroid-neo


if [ -d "neo-cli/Chain" ] && [ ! -f "neo-cli/Chain/$version" ] ; then
    echo "Old Chain Found...Scrubbing"
    rm -rf neo-cli/Chain/*
fi


if [ ! "$(ls -A neo-cli/Chain)" ] ; then
    chain=$(aws s3 ls s3://chainneo | awk '{print $4}' | sort -r | grep -m 1 $version)
    echo "Downloading: $chain"

    wget "https://s3.amazonaws.com/chainneo/$chain"    
 
    echo "Extracting: $chain"
    unzip "$chain"
    mv Chain/* neo-cli/Chain
    touch "neo-cli/Chain/$version"

    rm "$chain"
    rm -rf Chain

fi

./neo.sh
