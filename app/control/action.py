# (C) 2013 Dalek Labs

import cgi
import logging
import webapp2
import app.db.model

from google.appengine.ext import db

#
# Action handler (form POSTS)
#
class ActionHandler(webapp2.RequestHandler):
  def post(self):
    document = app.db.model.DocumentModel(url = cgi.escape(self.request.get('url')))
    db.put(document);
    logging.info('Created: [%s]' % (document.url))
