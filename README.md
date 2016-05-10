Bovespa End of Day data
=======

Bovespa EOD is a project that aims to promote Algorithm trading providing a JSON API for access end of day data to Bovespa stock market. To archive this goal, it downloads data directly from Bovespa website, stores in a Postgres database and provides an API to access this data.

Features
========
- Updates database from the last updated date.
- Provide a API to access spot / options / futures data

Installation
============

1. Installing requirements:
-----------------------
      $ pip install -r requirements.txt

2.  Configs
-----------------------
   2.1 It's necessary to database path: DATABASE_URL

   2.2. If you are running the database on your machine you need to install postgresql. In order to do that: 
    $  sudo apt-get install postgresql python-psycopg2 libpq-dev 

3.  Create schema
-----------------------
3.1 - Open the database and create a new database
3.2 - Run the script setup_database.sql


Running
============
1. The project has 2 servers: 
   updateserver -  that must be called whenever you want to update your database.
   restserver - Run the API service.
