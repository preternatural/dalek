# (C) 2013 Dalek Labs

import datetime
from google.appengine.ext import db

class DocumentModel(db.Model):
  url     = db.StringProperty()
  created = db.DateProperty()
  text    = db.Blob()
