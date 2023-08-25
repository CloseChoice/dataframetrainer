# Dataframetrainer
A WIP repository to build a data science programming tutor. This repository is capable to run locally 
and provides a in-browser Python experience. The website on which this should run later is not setup yet,
but will follow soon.

## Setup
It is assumed that Docker and python3.11 are installed and usable from the command-line.
In order to use docker without `sudo`:
```bash
# creates docker group
sudo groupadd docker
# adds current user to docker
sudo usermod -aG docker $USER
```
Afterwards just execute:
```bash
docker compose up
```
This starts the backend and the database. To start the frontend, use
```bash
cd frontend-svelte && npm run dev
```


#### Architecture of this repository
##### CI Pipelines
todo

##### A/B Testing
To improve the learning experience for the users and to tailer user-specific learning paths, we try [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) for the challenges provided to users. This is done in the following way:
- there are specific tables where users are divided into groups
- we provide just one endpoint `get_next_challenge` which takes the `user_id` as input and returns the id of the next challenge
- in the backend we implement a strategy per group, this is done in the implementation of `get_next_challenge`
- in the future we also plan to provide transparency over which strategy is applied to the user
