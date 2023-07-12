CREATE TABLE IF NOT EXISTS challenges(
    id varchar(100) NOT NULL
) TABLESPACE pg_default;

COPY challenges FROM PROGRAM 'ls /challenges/ | grep "^[[:upper:]]"';
