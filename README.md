# WHAT IT IS
A dumb webservice that uses a pre-shared key to authenticate users, and capture their IP address

# HOW TO INSTALL
Pull the repo

`docker-compose build`

`docker-compose run ipcatcher production.py`

`docker-compose up -d`

Optionally, create a local_config.py inside ipcatcher to modify the default settings (note: this is recommended. put a db in /data, etc)

# ROADMAP
Rename production.py to create_db.py

Update Dockerfile for ipcatcher to run create_db.py on build

Update project to reflect status as a series of small web apps (i.e., rename repo to wreck.haus)

Extract out nginx in a way that more apps can be added easily (such as secretsanta)

Update Vagrantfile to install docker-engine and compose on provision

Move away from sqlite to postgres

Create postgres container and share a volume between services

Create a master project that abstracts out nginx, because this will eventually house more apps/services
