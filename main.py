# (C) 2013 Dalek Labs

import os
import datetime
import logging
import time
import webapp2

import app.control.action
import app.control.query

from google.appengine.ext.webapp.template import render

#
# Main App handler.
#
class MainHandler(webapp2.RequestHandler):
  def get(self):
    context = {
      'dev': os.environ['SERVER_SOFTWARE'].find('Development') == 0,
      'status' : datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    }
    template = os.path.join(os.path.dirname(__file__), 'template/index.html')
    self.response.out.write(render(template, context))

#
# Main
#
app = webapp2.WSGIApplication(
  [
  ('/action', app.control.action.ActionHandler),
  ('/query',  app.control.query.QueryHandler),
  ('/', 		  MainHandler),
  ],
  debug=True)

