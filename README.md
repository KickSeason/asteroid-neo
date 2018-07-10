<p align="center">
  <img 
    src="https://assets.moonlight.io/vi/moonlight-logo-dark-800w.png" 
    width="400px"
    alt="Moonlight">
</p>


<p align="center" style="font-size: 48px;">
  <strong>Asteroid-Neo</strong>
</p>

<p align="center">
  A high-availability neo-cli service for asteroid.
</p>

Asteroid-Neo is designed to be run as either a stand-alone neo-cli instance or as a swarm with loadbalancing (Asteroid-loadBalancer).

#### The tool provides a number of enhancements over the conventional neo-cli deployment which targets improved uptime and deployment agility including:
- Fully functional microservice w/ easy deployment via docker
- Easy upgrade to new builds
- Automatic chain checkpointing and download
- Ability to auto-restart on failure
- (swarm) Load balancing across multiple nodes
- (swarm) Node redundancy

Currently, the container has two operating modes:
- <b>Slave:</b> will act in a similar fashion to neo-cli.
- <b>Master:</b> will occasionally pause the chain and push a checkpoint to the S3 bucket.  To run in master, you must provide the following environment variables at runtime:
   1. aws_access_key_id
   2. aws_secret_access_key

# Chain Syncing
When the container comes up, it will automatically search for an existing Chain directory to use.  If the directory is not found, or it was generated by an unsupported neo-cli version (requires new chain data), the node will pull the latest supported chain checkpoint  from S3.  If this fails, it will begin a full chain sync.

To force download of a new checkpoint, bring down the container and delete the Chain folder in `/var/lib/docker/volumes/asteroid-neo`, then run again.


# Individual Node Overview


## Using the registry
asteroid-neo is available on ECR and can be pulled using the following command:
```bash
sudo docker pull moonlightio/asteroid-neo
```

@TODO: migrate ECR to Moonlight AWS

## Building and Deploy
You can optionally build the container youself as well:

#### Clone the repo

```bash
git clone https://github.com/Moonlight-io/asteroid-neo.git
```
#### Build the container and tag it

```bash
cd asteroid-neo
docker build -t asteroid-neo .
```
#### Start the container with persistant storage

```bash
sudo docker run -d -p 10332:10332 -v Chain:/var/www/asteroid-neo/neo-cli/Chain asteroid-neo
```

or using the registry:

```bash
sudo docker run -d -p 10332:10332 -v Chain:/var/www/asteroid-neo/neo-cli/Chain moonlightio/asteroid-neo
```

<i><b>Note:</b> You will need to open port 10332 in your security group to access the RPC endpoint</i>

# High-Availability Swarm

This deployment method uses docker-machine to deploy a swarm of neo-cli instances.  The load-balancer service is used to guarantee that the highest available block in the swarm is returned.

<b>Note:</b> Load balancing in this funcationality has not yet been deployed.

## Locally:
<i><b>Note:</b> You will need to open ports 10332(TCP), 2376(TCP), 2377(TCP), 7946(TCP/UDP), and 4789(UDP) in your security group</i>

```bash
docker swarm init
docker stack deploy -c docker-compose.yml asteroid-neo --with-registry-auth
```

#### Bringing down the nodes

To bring down the nodes

```bash
docker stack rm asteroid-neo
docker swarm leave --force
```

##change
* replace aws to aliyun
* add sync.py to synchron chain data

> start  container use : 
```
 sudo docker run -d -p 10332:10332  --name node-master 
 ```
 ```-e  'aliyun_access_key_id=LTAIbqtbKzoXVtMq'   
 ```
 ```
 -e   'aliyun_secret_access_key=88RD6JfxDa56DDaAYtSU20Y6DvUCBa' 
 ```
 ```
 -e 'bucket_name=chainneo' 
 ```
 ```-e 'endpoint=oss-cn-hangzhou.aliyuncs.com'  
 ```
 ```-e 'runmaster=true' asteroid-neo
 ```