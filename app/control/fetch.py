"""FetchHandler, primary used to handle requests enqueued in task queue.

   (C) 2013 Dalek Labs
"""
import cgi
import logging
import webapp2

from google.appengine.api import taskqueue

from app.db.model import DocumentModel
from app.process.fetcher import Fetcher


class FetchHandler(webapp2.RequestHandler):
    def __init__(self):
        self.fetcher = Fetcher()
        
    def post(self):
        url = cgi.escape(self.request.get('url'))
        logging.info('Fetching %s' % url)
        text = self.fetcher.fetch_text_from_url(url)
        query = db.Query(DocumentModel)
        query.get('url =', url)
        doc = query.run()
        doc.text = text
        doc.put()
        taskqueue.add(url='/extract', params={'url': url})
