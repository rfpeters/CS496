import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Index(base_page.BaseHandler):
	def get(self):
		self.render('index.html')