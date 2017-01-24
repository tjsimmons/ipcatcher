# WHAT IT IS
A dumb webservice that uses a pre-shared key to authenticate users, and capture their IP address

# HOW TO INSTALL
Pull the repo
`docker-compose build`
`docker-compose run ipcatcher production.py`
`docker-compose up -d`

Optionally, create a local_config.py inside ipcatcher to modify the default settings (note: this is recommended. put a db in /data, etc)
