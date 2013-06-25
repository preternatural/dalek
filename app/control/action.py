"""ActionHandler for submitting a url.

   (C) 2013 Dalek Labs
"""
import cgi
import datetime
import logging
import webapp2

import app.db.model

from google.appengine.api import taskqueue
from google.appengine.ext import db

#
# Action handler (form POSTS)
#
class ActionHandler(webapp2.RequestHandler):
  def post(self):
    document = app.db.model.DocumentModel(
      url = cgi.escape(self.request.get('url')), 
      created = datetime.datetime.now(),
      )
    db.put(document);
    taskqueue.add(url='/fetch', params={'url': document.url})
    logging.info('Created: [%s]' % document.url)
