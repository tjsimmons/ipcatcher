# WHAT IT IS
A dumb webservice that uses a pre-shared key to authenticate users, and capture their IP address

# HOW TO INSTALL
`git pull https://github.com/tjsimmons/ipcatcher.git`

`cd ipcatcher`

`docker-compose build`

`docker-compose up -d`

Optionally, create a local_config.py inside ipcatcher to modify the default settings (note: this is recommended. put a db in /data, etc)

# ROADMAP
1. Add logging for nginx
  1. Create logs directory within project root
  1. Modify docker-compose.yml to add a new volume to nginx that points logs to /var/logs

1. Update project to reflect status as a series of small web apps (i.e., rename repo to wreck.haus)

1. Update Vagrantfile to install docker-engine and compose on provision

1. Move away from sqlite to postgres

  1. Create postgres container and share a volume between services

1. Create a master project that abstracts out nginx, because this will eventually house more apps/services
