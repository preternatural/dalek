# (C) 2013 Dalek Labs

import datetime
from google.appengine.ext import db

class DocumentModel(db.Model):
    url     = db.StringProperty()
    created = db.DateProperty()
    # Todo(jeff): having a single blob for text is a fine starting point but
    # diffbot provides some structure: title, author, date, text, tags & links
    # to included media. No sense throwing all of that away.
    text    = db.Blob()

