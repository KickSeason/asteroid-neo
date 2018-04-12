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
  A neo-cli service for asteroid.
</p>


## Overview


## Pull and Deploy
asteroid-neo is available on ECR and can be pulled using the following command:
```bash
sudo docker pull 340431872443.dkr.ecr.us-east-1.amazonaws.com/asteroid-neo
```

@TODO: migrate ECR to Moonlight AWS

## Build and Deploy


#### Clone the repo

```bash
git clone https://github.com/Moonlight-io/asteroid-neo.git
```
#### Build the container and tag it

```bash
cd asteroid-neo
docker build -t asteroid-neo .
```
#### Start the container with the port binding

```bash
docker run -d -p 10332:10332 asteroid-neo
```

<i><b>Note:</b> You will need to open port 10332 in your security group</i>
