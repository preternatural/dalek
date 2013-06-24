# (C) 2013 Dalek Labs

import cgi
import json
import logging
import webapp2
import app.db.model

from google.appengine.ext import db

#
# JSON Query handler
#
class QueryHandler(webapp2.RequestHandler):
  def get(self):
    # TODO(burdon): Filter documents.
    query = app.db.model.DocumentModel.all()
    
    # Create JSON list.
    items = []
    for entity in query.run():
      item = {
        'url' : entity.url
      }
      items.append(item)
    
    str = json.dumps({
      'item' : items
    })

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(str)
