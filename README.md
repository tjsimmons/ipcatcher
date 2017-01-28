# WHAT IT IS
A dumb webservice that uses a pre-shared key to authenticate users, and capture their IP address

# HOW TO INSTALL
`git pull https://github.com/tjsimmons/ipcatcher.git`

`cd ipcatcher`

`docker-compose build`

`docker-compose up -d`

# ROADMAP
1. Set up staticfile serving with nginx (use collectstatic)

1. Figure out docker-compose logging and multiple Compose files

1. Create a master project that abstracts out nginx, because this will eventually house more apps/services
