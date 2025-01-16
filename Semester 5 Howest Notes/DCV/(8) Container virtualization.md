# General 
Containers != VMs
Containers are processes that can be viewed, in the processes list. This are **isolated processes**
It is a OS level virtualization (multiple user-space instances).
Linux containers will not run on Windows.
In Linux, containers are being created by using bash commands.

# Docker
Docker is a container engine, that allows me to make OS level virtualization.
I can pull images, to create containers, from the docker servers.
This images also have dockerfiles, that are responsible to create the appropriate settings for these containers, or this one can do a separate actions that we are going to set it to.
## Docker compose
This tool is a part of docker, and it allows to "create multiple containers" at the same time, which can for example launch a WordPress with database.
## Docker server
We have a daemon running of daemon, and execution of commands is actually talking to the API of the Docker.
In the meantime, while executing commands, the docker talks to **containerd**, then **runc** and then to the container itself, before something changes.
# Podman
It is a daemonless engine. It has rootless containers.
Podman can do pretty much the same things as Docker, and even use the same images (by specifying that we need them from docker.io/image.name)
# LXC/LXD/Incus
This are Linuxcontainers, which is yet again software for containerization.
LXC is LinuX Containers, and it works more towards system containers.
LXD is a addon to LXC. It is more like a user interface to manage containers. Containers can be managed over the network through a REST API.
