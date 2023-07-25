# Dataframetrainer
a WIP repository to build a data science programming tutor

# Static File Server
- `npm install -g http-server`
- `http-server static-challenges`
- `cd frontend-svelte`
- `npm install`
- `npm run dev`
- visit `http://localhost:5173/challenge/addition`

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

# Commands
```bash
# Will make the website available on localhost:5173
make dev

# Build the production version of the website on localhost:3000
make prod
```
