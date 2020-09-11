# Extended .env for Docker-Compose

If you are like me, you have a lot of containers in a docker-compose stack, each of which have many variables within their configuration. This can make maintenance unruly if your topology changes. Using a .env file to isolate some configuration variables certainly helps, but I realized that it lacked one important feature: being able to use variables within the declaration of other variables. This may seem like a trivial problem, but consider the following situation. You have a complex directory structure for your stack that hinges on one major root directory. If you change this directory, you either have to edit many variables in a .env file, or you have to keep much more information in your docker-compose.yml file.

Extended .env solves this by allowing the user to create a .env file where "<" and ">" are used to encase variables defined above in the file. These are then resolved to the full value once a normal .env is generated.
For example, a .eenv file containing:
```
DOCKER_DIRECTORY=/home/user/docker
CONTAINER_DIRECTORY=<DOCKER_DIRECTORY>/container
```
Resolves to a .env file containing:
```
DOCKER_DIRECTORY=/home/user/docker
CONTAINER_DIRECTORY=/home/user/docker/container
```
Any line that does not contain an "=" not added to the resultant .env file, so comments and empty lines in .eenv files are acceptable. If you add a comment after a variable declaration, it will currently still be included in the resultant .env file.
