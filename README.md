# WHAT IT IS
A dumb webservice that uses a pre-shared key to authenticate users, and capture their IP address

# HOW TO INSTALL
`git pull https://github.com/tjsimmons/ipcatcher.git`

`cd wreck.haus`

`docker-compose build`

`docker-compose up -d`

# ROADMAP
1. Move from flask to Django. Flask feels weird, and I know Django.

1. Figure out docker-compose logging and multiple Compose files

1. Create a master project that abstracts out nginx, because this will eventually house more apps/services
