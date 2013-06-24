# (C) 2013 Dalek Labs

import datetime
from google.appengine.ext import db

class DocumentModel(db.Model):
  created   = db.DateTimeProperty()
  processed = db.DateTimeProperty()
  url       = db.StringProperty()
  text      = db.Blob()
