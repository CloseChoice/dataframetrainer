import psycopg2

import click
import os
import time

DEFAULT_ELO = 700
TABLE_ORDER = ["users", "sessions", "challenges", "user_challenges", "challenge_elo"]
ROLES = ["roles"]
FUNCTIONS = ["authentication_functions"]

def check_ping(hostname):
    while True:
        print("Checking network connection...")
        response = os.system("ping -c 1 " + hostname)
        # and then check the response...
        if response == 0:
            print("ping received")
            # sleep for 3 seconds so that db has time to set up
            time.sleep(3)
            return
        time.sleep(5)

@click.command()
@click.option("--port", default=5432, help="Port of the database")
@click.option("--password", default="example", help="Password of the database")
@click.option("--user", default="postgres", help="User of the database")
@click.option("--host", default="db", help="Host of the database")
@click.option("--dbname", default="postgres", help="Name of the database")
def run(port, dbname, password, user, host):
    # read the sql file to create challenges
    check_ping(host)
    conn = psycopg2.connect(
        host=host, dbname=dbname, user=user, password=password, port=port
    )
    # conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='secret', port=5434)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    # make sure that all tables are created
    # todo: add db_create tables aswell
    for role in ROLES:
        with open(f"sql/{role}.sql") as f:
            cursor.execute(f.read())

    for table in TABLE_ORDER:
        with open(f"sql/{table}.sql") as f:
            cursor.execute(f.read())

    for function in FUNCTIONS:
        with open(f"sql/{function}.sql") as f:
            cursor.execute(f.read())

    for challenge in os.listdir("challenges"):
        # ignore files that are not challenges
        if not challenge[0].isupper():
            continue
        # Add challenge to challenges table
        cursor.execute(f"select id from challenges where id = '{challenge}'")
        if (k := cursor.fetchone()) is None:
            cursor.execute(f"insert into challenges (id) values ('{challenge}')")
        # Update challenge_elo table
        cursor.execute(f"select * from challenge_elo where challenge_id = '{challenge}'")
        fetched_elo = cursor.fetchone()
        if fetched_elo is None:
            cursor.execute(
                f"insert into challenge_elo (elo, challenge_id) values ({DEFAULT_ELO}, '{challenge}')"
            )
    conn.commit()


if __name__ == "__main__":
    run()
