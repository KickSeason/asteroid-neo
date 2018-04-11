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


##Overview




##Deploying

```bash

#### Clone the repo
git clone https://github.com/Moonlight-io/asteroid-neo.git

#### Build the container and tag it
cd asteroid-neo
docker build -t asteroid-neo .

### Start the container with the port binding
docker run -d -p 10332:10332 asteroid-neo
```

<i><b>Note:</b> You will need to open port 10332 in your security group</i>
