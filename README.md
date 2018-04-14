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



# Chain Syncing
When the container comes up, it will automatically search for an existing Chain directory to use.  If the directory is not found, it will attempt
to pull the latest checkpoint chain from S3.  If this fails, it will begin a full chain sync.

To force a full chain sync (if the version check fails), bring down the container and delete the Chain folder in `/var/lib/docker/volumes/asteroid-neo`, then run again.


# Individual Node Overview


## Using the registry
asteroid-neo is available on ECR and can be pulled using the following command:
```bash
sudo docker pull 340431872443.dkr.ecr.us-east-1.amazonaws.com/asteroid-neo
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
sudo docker run -d -p 10332:10332 -v Chain:/var/www/asteroid-neo/neo-cli/Chain 340431872443.dkr.ecr.us-east-1.amazonaws.com/asteroid-neo
```

<i><b>Note:</b> You will need to open port 10332 in your security group to access the RPC endpoint</i>

# High-Availability Swarm

This deployment method uses docker-machine to deploy a swarm of neo-cli instances.  The load-balancer service is used to guarantee that the highest available block in the swarm is returned.

## Locally:
<i><b>Note:</b> You will need to open port 10332 in your security group</i>

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
