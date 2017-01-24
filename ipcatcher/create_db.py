#!/bin/python

from ipcatcher import db

try:
  db.create_all()
except Exception as e:
  print(e)
  pass
