# WHAT IT IS
A dumb webservice that uses a pre-shared key to authenticate users, and capture their IP address

# HOW TO INSTALL
`git pull https://github.com/tjsimmons/ipcatcher.git`

`cd ipcatcher`

`docker-compose build`

`docker-compose up -d`

# ROADMAP
1. Double-check proxy pass settings for remote IP address
    1. could also be a Django issue, with the request metadata being pulled
1. Figure out docker-compose logging to a persistent datastore
