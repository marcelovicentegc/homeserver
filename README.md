# homeserver <!-- omit in toc -->

This repository contains the code that runs on my homeserver. 

- [Getting started](#getting-started)
  - [Requirements](#requirements)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Development instructions](#development-instructions)
  - [Production instructions](#production-instructions)

## Getting started

### Requirements

Before you start, make sure you have the following hardware and software installed on your development and production machines (this project assumes that your development machine is not your production machine).

#### Hardware

You'll need at least 4GB of RAM and 2 CPU cores to run all services, as well as a configurable router. This code is running on a Raspberry Pi 5 with 8GB of RAM as the host machine attached to a TP Link ER706W.

#### Software

You'll need Docker, Docker Compose and Python installed on your development and production machines, and Node installed on your development machine just for the sake of simplicity for running some scripts that enhance DX.

### Development instructions

Once you've cloned the repository, you can start the services on your local machine with the following command:

```bash
npm run dev
```

### Production instructions

To deploy the services to your production machine, you'll need to have SSH access to it.

This project expects two environment variables to be set on your development machine in order to operate your production machine, make sure to set them on your user profile (.bashrc, .zshrc, etc):

```bash
export HS_USER=your_user
export HS_HOST=your_host
```
