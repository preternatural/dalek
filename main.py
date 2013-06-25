# (C) 2013 Dalek Labs

import os
import datetime
import time
import webapp2

from google.appengine.ext.webapp.template import render

import app.control.action
import app.control.extract
import app.control.fetch
import app.control.query


#
# Main App handler.
#
class MainHandler(webapp2.RequestHandler):
    def get(self):
        context = {
          'dev': os.environ['SERVER_SOFTWARE'].find('Development') == 0,
          'status' : datetime.datetime.fromtimestamp(time.time()).strftime(
            '%Y-%m-%d %H:%M:%S')
            }
        template = os.path.join(os.path.dirname(__file__),
                                'template/index.html')
        self.response.out.write(render(template, context))

#
# Main
#
app = webapp2.WSGIApplication(
  [
  ('/action', app.control.action.ActionHandler),
  ('/extract',  app.control.extract.ExtractHandler),
  ('/fetch',  app.control.fetch.FetchHandler),
  ('/query',  app.control.query.QueryHandler),
  ('/', 		  MainHandler),
  ],
  debug=True)
