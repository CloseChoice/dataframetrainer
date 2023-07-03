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
make build
docker compose up
```
This will build the necessary docker containers and launch them. The frontend accessed through the `frontend/index.html` file.
We recommend using the [live server extension for vscode](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
but any other server also works.
