import psycopg2

import click
import os
import time

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
    print("start inserting tables")
    # make sure that all tables are created
    cursor = conn.cursor()
    for sql_file in os.listdir("sql"):
        print("Try to insert into table: ", sql_file)
        with open(f"sql/{sql_file}") as f:
            cursor.execute(f.read())
    print("Committing")
    conn.commit()
    print("Successfully committed")


if __name__ == "__main__":
    run()
