- more information:
  - [ ] https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart#step-5-opening-a-postgres-prompt-with-the-new-role
Use postgres 15.2 Docker image
Run with:
 - sudo docker run -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=tobias postgres:15.3

 - sudo docker run --user tobias -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=tobias postgres:15.3

 - sudo docker run postgres:15



 - test:
 sudo docker run --name pgsql-dev -e POSTGRES_PASSWORD=test1234 -p 5433:5432 postgres
 sudo docker exec -it pgsql-dev bash
 psql -h localhost -U postgres

 - restart (data is saved in container!!!):
 sudo docker restart pgsql-dev



 NOTE WHITESPACES AND ORDERING OF KEYS:
 Because the json type stores an exact copy of the input text, it will preserve semantically-insignificant white space between tokens, as well as the order of keys within JSON objects. Also, if a JSON object within the value contains the same key more than once, all the key/value pairs are kept. (The processing functions consider the last value as the operative one.) By contrast, jsonb does not preserve white space, does not preserve the order of object keys, and does not keep duplicate object keys. If duplicate keys are specified in the input, only the last value is kept.

#### Commands and Stuff
postgres commands:
\c <database-name> -> select db
\l -> list databases
\dt -> list tables in currently selected db

 create jsonb column:
 create table amsterdam
(
   id       integer primary key,
   payload  jsonb not null default '{}'::jsonb
);

We are interested in a not null json column:

 create table challenges
(
   id       integer primary key,
   initial_task     json not null
);

insert into challenges values (1, '"data_frames(columns=[column(''ActualDate'', dtype=np.dtype(''datetime64[ns]''))], index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=1000), dtype=int))"'::json);


 create table challenges
(
   id       integer primary key,
   initial_task     json not null,
   possible_solution json not null
);


insert into challenges (id, initial_task, possible_solution) values (1,
                               '"data_frames(columns=[column(''ActualDate'', dtype=np.dtype(''datetime64[ns]''))], index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=1000), dtype=int))"'::json,
                               '"def transform(df):df[''CalcEnd''] = df[''ActualDate''] + pd.offsets.MonthEnd(0);return df"'::json
                               );
