"""ExtractHandler, primary used to handle requests enqueued in task queue.

   (C) 2013 Dalek Labs

   Todo(jeff): figure out how to run nltk on gae
"""
import cgi
import logging
import webapp2

from google.appengine.ext import db

from app.db.model import DocumentModel
# from app.process.entities import EntityExtractor


class ExtractHandler(webapp2.RequestHandler):
    def __init__(self):
        #self.extractor = EntityExtractor()
        pass
    
    def post(self):
        url = cgi.escape(self.request.get('url'))
        logging.info('Extracting entities from %s' % url)
        query = db.Query(DocumentModel)
        query.get('url =', url)
        doc = query.run()
        text = self.extractor.extract_named_entities(doc.text)
        # Todo(jeff): save the entities somewhere, but that requires a model...
