import psycopg2

import os
import time

DEFAULT_ELO = 700

EXTENSIONS = ["uuid_ossp"]

TABLE_ORDER = ["users", "challenges", "users_challenges", 
               # THESE ARE THE A/B TESTING TABLES
                "a_b_testing/groups", "a_b_testing/users_groups",
                "a_b_testing/strategies/challenges_elo", "a_b_testing/strategies/users_elo"]

ROLES = ["roles"]
FUNCTIONS = []


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


def run():
    # read the sql file to create challenges
    host = os.environ["HOST"]
    check_ping(host)
    conn = psycopg2.connect(
        host=host,
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["PASSWORD"],
        port=os.environ["PORT"],
    )
    # make sure that all tables are created
    cursor = conn.cursor()
    print("Creating extensions")
    for extension in EXTENSIONS:
        with open(f"sql/{extension}.sql") as f:
            try:
                cursor.execute(f.read())
            except psycopg2.errors.DuplicateFunction:
                print("function already exists. Initiating rollback...")
                conn.rollback()
                pass

    print("Creating functions")
    for function in FUNCTIONS:
        with open(f"sql/{function}.sql") as f:
            cursor.execute(f.read())

    print("Creating tables")
    for table in TABLE_ORDER:
        with open(f"sql/{table}.sql") as f:
            print(f"create table {table}")
            cursor.execute(f.read())

    print("Update challenges")
    for challenge in os.listdir("challenges"):
        # ignore files that are not challenges
        if not challenge[0].isupper():
            continue
        # Add challenge to challenges table
        cursor.execute(f"select id from challenges where id = '{challenge}'")
        if (k := cursor.fetchone()) is None:
            cursor.execute(f"insert into challenges (id) values ('{challenge}')")
        # Update challenges_elo table
        cursor.execute(
            f"select * from challenges_elo where challenge_id = '{challenge}'"
        )
        fetched_elo = cursor.fetchone()
        if fetched_elo is None:
            cursor.execute(
                f"insert into challenges_elo (elo, challenge_id) values ({DEFAULT_ELO}, '{challenge}')"
            )
    print("Committing")
    conn.commit()
    print("Successfully committed")


if __name__ == "__main__":
    run()
