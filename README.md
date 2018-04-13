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
docker stack deploy -c docker-compose.yml asteroid-neo
```

#### Bringing down the nodes

To bring down the nodes

```bash
docker stack rm asteroid-neo
docker swarm leave --force
```
