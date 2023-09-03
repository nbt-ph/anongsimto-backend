import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

# database connection
try:
    conn = psycopg2.connect(database=os.environ.get('DB_NAME'),
                            host=os.environ.get('DB_HOST'),
                            user=os.environ.get('DB_USER'),
                            port=os.environ.get('DB_PORT'))
except:
    print("unable to connect to db")

cursor = conn.cursor()
try:
    cursor.execute(
        """
CREATE TABLE "prefixes"(
    "prefix" VARCHAR(255) NOT NULL,
    "carrier" VARCHAR(255) NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
CREATE INDEX "prefixes_carrier_index" ON
    "prefixes"("carrier");
ALTER TABLE
    "prefixes" ADD PRIMARY KEY("prefix");
CREATE TABLE "carriers"(
    "name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "carriers" ADD PRIMARY KEY("name");
ALTER TABLE
    "prefixes" ADD CONSTRAINT "prefixes_carrier_foreign" FOREIGN KEY("carrier") REFERENCES "carriers"("name");
""")
except:
    print("unable to setup db")

# TODO: add script for loading initial carriers
# INSERT INTO "carriers"("name", "created_at", "updated_at") VALUES('smart', 'NOW()', 'NOW()')

conn.commit()

cursor.close()
conn.close()
