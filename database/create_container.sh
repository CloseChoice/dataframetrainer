# sudo docker run -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=tobias postgres:15.2
mkdir -p database
# todo: don't expose secrets to git: e.g. have a look at https://hub.docker.com/_/postgres
# https://stackoverflow.com/questions/22651647/docker-and-securing-passwords
# https://docs.docker.com/compose/environment-variables/env-file/
# export private files
# export $(cat files/.env | xargs)
POSTGRES_PW=secret
POSTGRES_PORT=5435
VOLUME_NAME=dftrainer_db
docker container stop pgsql-test
docker container rm pgsql-test
docker volume rm $VOLUME_NAME
# we need the double slash to make it work for git bash
docker run --detach --name pgsql-test \
     --mount type=volume,src=$VOLUME_NAME,dst=//var/lib/postgresql/data \
     -e POSTGRES_PASSWORD=$POSTGRES_PW \
     -p $POSTGRES_PORT:5432 postgres:15.3
source .venv/bin/activate
sleep 1
python write_all_challenges_to_db.py --port $POSTGRES_PORT --password $POSTGRES_PW
