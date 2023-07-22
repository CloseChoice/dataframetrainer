import psycopg2

import click
import os
import time

DEFAULT_ELO = 700
TABLE_ORDER = ["users", "accounts", "sessions", "verification_tokens", "challenges", "user_challenges", 
               # THESE ARE THE A/B TESTING TABLES
                "a_b_testing/groups", "a_b_testing/users_groups",
                "a_b_testing/strategies/challenge_elo", "a_b_testing/strategies/users_elo"]
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
    # make sure that all tables are created
    cursor = conn.cursor()
    for role in ROLES:
        with open(f"sql/{role}.sql") as f:
            # todo: this wastes the cursor if the role already exists,
            # and there is no possibility to add something like `if not exists` to a role definition AFAIK
            try:
                cursor.execute(f.read())
            except psycopg2.errors.DuplicateObject as e:
                # roles are already defined
                conn.rollback()
            except Exception as e:
                print(e)
                raise ValueError(e)

    for function in FUNCTIONS:
        with open(f"sql/{function}.sql") as f:
            cursor.execute(f.read())

    for table in TABLE_ORDER:
        with open(f"sql/{table}.sql") as f:
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
